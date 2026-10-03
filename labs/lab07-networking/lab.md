# Lab 7 — Docker Networking — Custom Bridge, DNS & Port Mapping

**Folder:** `labs/lab07-networking/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-03-docker-networking

## Goal

Connect two containers the way real apps do: TaskBoard reaching a Redis cache by name over a custom bridge network. You'll see why a custom network (with built-in DNS) beats the default bridge, then publish the app to the host with port mapping.

## What you'll build

TaskBoard reaches Redis by DNS name on a custom network; publish ports to the host.


---

## Step 1 — Why a custom network

On the **default** bridge, containers can only reach each other by IP address (which changes on restart). On a **custom** bridge network, Docker provides automatic DNS, so a container can reach another by its **name** — exactly what a web app needs to find its database or cache.


---

## Step 2 — Create a network and a Redis cache

```bash
docker network create tasknet
docker run -d --name redis --network tasknet redis:7-alpine
```


---

## Step 3 — Run TaskBoard on the same network

TaskBoard reads `REDIS_HOST` to find the cache. Set it to the **container name** `redis` — DNS on `tasknet` resolves it automatically:

```bash
docker run -d --name tb --network tasknet -p 8080:5000 \
  -e REDIS_HOST=redis taskboard:1.0
curl http://localhost:8080      # 'visits' counter increments on each load
curl http://localhost:8080
```

Prove the DNS name resolves from inside the app container:

```bash
docker exec tb getent hosts redis   # resolves to redis's IP on tasknet
```


---

## Step 4 — Port mapping (host access)

`-p 8080:5000` maps host port 8080 to the container's 5000. Run a second instance on a different host port — same image, two endpoints:

```bash
docker run -d --name tb-b --network tasknet -p 8081:5000 \
  -e REDIS_HOST=redis taskboard:1.0
curl http://localhost:8081/health
docker rm -f tb tb-b redis
docker network rm tasknet
```

> **Note:** Because both TaskBoard instances share one Redis on the network, the visit counter is shared across them — your first taste of stateful, multi-container apps (which Compose and Kubernetes automate).


---

> ✅ **Test it:** Reloading http://localhost:8080 increases the `visits` count (served from Redis), and `docker exec tb getent hosts redis` resolves the `redis` name to an IP on the custom network.
