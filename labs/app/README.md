# TaskBoard — the course sample application

**TaskBoard** is a small Flask task-tracker web app that threads through every lab in
this course. The same source is reused (and progressively wired up) from a single
container all the way to a full-stack Docker Compose app and a Kubernetes deployment.

| File | Purpose |
|---|---|
| `app.py` | The Flask web app (board UI + JSON API + `/health`). Degrades gracefully: JSON file store by default, PostgreSQL if `DATABASE_URL` is set, Redis visit-counter if `REDIS_HOST` is set. |
| `templates/index.html` | The board UI (list tasks, add a task, mark done). |
| `cli.py` | `taskboard-cli` — a companion CLI used in **Lab 05 (CMD vs ENTRYPOINT)**. |
| `requirements.txt` | `flask`, `redis`, `psycopg2-binary`. |

## Runtime configuration (environment variables)

| Variable | Default | Used in |
|---|---|---|
| `APP_ENV` | `development` | Lab 08 — environment config |
| `APP_TITLE` | `TaskBoard` | Lab 08 — environment config |
| `DATA_DIR` | `./data` | Lab 06 — volumes (set to `/data` and mount a volume) |
| `REDIS_HOST` / `REDIS_PORT` | — / `6379` | Lab 07, 11 — visit counter in Redis |
| `DATABASE_URL` | — | Lab 12 — tasks stored in PostgreSQL |
| `PORT` | `5000` | container port |

Most Docker labs build this app once (Lab 03) and reuse the resulting `taskboard`
image; the Compose and Kubernetes labs ship their own copies so each lab folder is
self-contained.
