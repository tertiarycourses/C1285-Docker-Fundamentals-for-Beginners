"""
TaskBoard — a small Flask task-tracker web app used throughout the course.

It is written to "degrade gracefully" so the SAME code works in every lab:

  * Tasks are stored in a JSON file under DATA_DIR (default ./data).
    Set DATA_DIR=/data and mount a volume to make them persist (Lab 06).
  * If DATABASE_URL is set, tasks are stored in PostgreSQL instead of the
    JSON file (Lab 12 full-stack Compose / Kubernetes).
  * If REDIS_HOST is set, a page-visit counter is kept in Redis so it is
    shared across replicas (Lab 07 networking, Lab 11 Compose).
  * APP_ENV and APP_TITLE configure the app at runtime (Lab 08).

Endpoints:
  GET  /            -> HTML board (list tasks + add form)
  POST /add         -> add a task, redirect back to /
  POST /done/<id>   -> mark a task done
  GET  /api/tasks   -> tasks as JSON
  GET  /health      -> {"status": "ok"}  (used by Compose/K8s health checks)
"""
import os
import json
from datetime import datetime, timezone
from flask import Flask, request, redirect, url_for, jsonify, render_template

APP_ENV = os.environ.get("APP_ENV", "development")
APP_TITLE = os.environ.get("APP_TITLE", "TaskBoard")
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(__file__), "data"))
DATABASE_URL = os.environ.get("DATABASE_URL")
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))

app = Flask(__name__)

# ---------------------------------------------------------------- optional Redis
_redis = None
if REDIS_HOST:
    try:
        import redis  # type: ignore
        _redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT,
                             socket_connect_timeout=1, decode_responses=True)
        _redis.ping()
    except Exception as exc:  # pragma: no cover - lab resilience
        print(f"[TaskBoard] Redis unavailable ({exc}); using local visit count")
        _redis = None

# ---------------------------------------------------------------- optional Postgres
_pg = None
if DATABASE_URL:
    try:
        import psycopg2  # type: ignore
        _pg = psycopg2.connect(DATABASE_URL)
        _pg.autocommit = True
        with _pg.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS tasks ("
                "id SERIAL PRIMARY KEY, text TEXT NOT NULL, "
                "done BOOLEAN DEFAULT FALSE, created TIMESTAMPTZ DEFAULT now())")
    except Exception as exc:  # pragma: no cover - lab resilience
        print(f"[TaskBoard] Postgres unavailable ({exc}); using JSON file store")
        _pg = None


# ---------------------------------------------------------------- task storage
def _json_path():
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, "tasks.json")


def load_tasks():
    if _pg:
        with _pg.cursor() as cur:
            cur.execute("SELECT id, text, done FROM tasks ORDER BY id")
            return [{"id": r[0], "text": r[1], "done": r[2]} for r in cur.fetchall()]
    try:
        with open(_json_path()) as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def add_task(text):
    if _pg:
        with _pg.cursor() as cur:
            cur.execute("INSERT INTO tasks (text) VALUES (%s)", (text,))
        return
    tasks = load_tasks()
    next_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": next_id, "text": text, "done": False})
    with open(_json_path(), "w") as fh:
        json.dump(tasks, fh, indent=2)


def mark_done(task_id):
    if _pg:
        with _pg.cursor() as cur:
            cur.execute("UPDATE tasks SET done = TRUE WHERE id = %s", (task_id,))
        return
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
    with open(_json_path(), "w") as fh:
        json.dump(tasks, fh, indent=2)


def bump_visits():
    if _redis:
        return _redis.incr("taskboard:visits")
    return None


# ---------------------------------------------------------------- routes
@app.route("/")
def index():
    visits = bump_visits()
    return render_template("index.html", title=APP_TITLE, env=APP_ENV,
                           tasks=load_tasks(), visits=visits,
                           store=("postgres" if _pg else "file"),
                           cache=("redis" if _redis else "none"))


@app.route("/add", methods=["POST"])
def add():
    text = (request.form.get("text") or "").strip()
    if text:
        add_task(text)
    return redirect(url_for("index"))


@app.route("/done/<int:task_id>", methods=["POST"])
def done(task_id):
    mark_done(task_id)
    return redirect(url_for("index"))


@app.route("/api/tasks")
def api_tasks():
    return jsonify(load_tasks())


@app.route("/health")
def health():
    return jsonify(status="ok", env=APP_ENV,
                   store=("postgres" if _pg else "file"),
                   time=datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    print(f"[TaskBoard] starting env={APP_ENV} title={APP_TITLE} "
          f"store={'postgres' if _pg else 'file'} cache={'redis' if _redis else 'none'}")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
