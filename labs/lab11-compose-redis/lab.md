# Lab 11 — Docker Compose — Multi-Service (Web + Redis)

**Folder:** `labs/lab11-compose-redis/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-05-docker-compose

## Goal

Add a second service. Compose puts both containers on one network and gives each a DNS name equal to its service name, so TaskBoard reaches Redis at host `redis` with zero manual networking. The visit counter is now shared and survives restarts.

## What you'll build

Run TaskBoard + Redis with Compose; services find each other by name automatically.


---

## Step 1 — Two services, one file

```yaml
services:
  web:
    build: .
    ports: ["8080:5000"]
    environment:
      - REDIS_HOST=redis     # <-- the other service's name
    depends_on: [redis]
  redis:
    image: redis:7-alpine
    volumes: [redis-data:/data]
volumes:
  redis-data:
```

Compose creates a network automatically and registers each service under its name, so `REDIS_HOST=redis` just works — no IPs, no `docker network create`.


---

## Step 2 — Run the full lifecycle

```bash
docker compose pull        # pulls redis:7-alpine
docker compose up -d
docker compose ps
curl http://localhost:8080 && curl http://localhost:8080  # visits go up
```


---

## Step 3 — Prove persistence, then tear down

```bash
docker compose restart web
curl http://localhost:8080   # counter kept (it lives in redis-data)
docker compose down          # keep the volume
docker compose down -v       # remove the redis-data volume too
```

> **Note:** `depends_on` controls **start order**, not readiness — the next lab adds a **health check** so the web service waits until the database is truly ready.


---

> ✅ **Test it:** Reloading http://localhost:8080 increments the visit counter, and the count survives `docker compose restart web` because it is stored in the `redis-data` volume.
