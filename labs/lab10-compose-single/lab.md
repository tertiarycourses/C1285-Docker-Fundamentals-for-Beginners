# Lab 10 — Docker Compose — Single Service

**Folder:** `labs/lab10-compose-single/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-05-docker-compose

## Goal

Replace long `docker run` commands with a single declarative file. You'll define TaskBoard in a docker-compose.yml and manage it with the compose lifecycle: pull, up, ps, logs, down.

## What you'll build

Define TaskBoard in docker-compose.yml; manage it with pull / up / ps / logs / down.


---

## Step 1 — The compose file

```yaml
services:
  web:
    build: .            # build from the Dockerfile in this folder
    ports:
      - "8080:5000"     # host:container
    environment:
      - APP_ENV=development
      - APP_TITLE=TaskBoard (Compose)
```


---

## Step 2 — The Compose lifecycle

```bash
docker compose pull        # pull any pre-built images (none to build here)
docker compose up -d       # build if needed and start in the background
docker compose ps          # service status
docker compose logs web    # logs for the web service
curl http://localhost:8080/health
```


---

## Step 3 — Tear down

```bash
docker compose down        # stop and remove containers + network
docker compose down -v     # also remove named volumes (full reset)
```

> **Note:** `docker compose up -d` is idempotent — re-run it after editing the file and Compose only changes what's needed. One file replaces a page of `docker run` flags.


---

> ✅ **Test it:** `docker compose up -d` starts the service and http://localhost:8080 serves TaskBoard titled 'TaskBoard (Compose)'; `docker compose down` removes it cleanly.
