# Lab 12 — Docker Compose — Full-Stack (Web + PostgreSQL + Redis)

**Folder:** `labs/lab12-compose-fullstack/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-05-docker-compose

## Goal

Build the complete TaskBoard stack: the web app backed by PostgreSQL for tasks and Redis for the visit counter, with a health check so the app starts only once the database is ready. This is the architecture you'll deploy to Kubernetes later today.

## What you'll build

Run TaskBoard + Postgres + Redis with healthchecks and condition-based depends_on.


---

## Step 1 — The full stack

Three services: `web` (TaskBoard), `db` (PostgreSQL, storing tasks), and `redis` (visit counter). The web service waits for the database's **health check** to pass before it starts, so it never crashes on a not-yet-ready database.

```yaml
services:
  web:
    build: .
    ports: ["8080:5000"]
    environment:
      - DATABASE_URL=postgresql://taskboard:secret@db:5432/taskboard
      - REDIS_HOST=redis
    depends_on:
      db: { condition: service_healthy }
      redis: { condition: service_started }
  db:
    image: postgres:16-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U taskboard"]
      interval: 5s
      retries: 5
  redis: { image: redis:7-alpine }
```


---

## Step 2 — Run the lifecycle

```bash
docker compose pull        # pulls postgres + redis
docker compose up -d        # builds web, waits for db health, then starts web
docker compose ps           # db shows (healthy)
docker compose logs web
```


---

## Step 3 — Verify tasks persist in Postgres

```bash
# add tasks at http://localhost:8080, then prove they're in the DB:
docker compose exec db psql -U taskboard -c 'SELECT id, text, done FROM tasks;'
docker compose restart web
curl http://localhost:8080/api/tasks   # tasks still there (in Postgres)
```


---

## Step 4 — Tear down

```bash
docker compose down         # stop & remove containers + network
docker compose down -v      # also drop the pgdata volume
```

> **Note:** This web + database + cache shape is the canonical cloud app. Later today you'll deploy this very app to Kubernetes — as Pods, a Deployment, a Service, and persistent storage.


---

> ✅ **Test it:** `docker compose ps` shows `db` as `(healthy)`, tasks added in the browser appear in `SELECT * FROM tasks`, and they survive `docker compose restart web`.
