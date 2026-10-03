# Lab 1 — Docker Commands — Run & Manage Containers

**Folder:** `labs/lab01-docker-commands/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-01-docker-fundamentals

## Goal

Get comfortable with the core Docker commands by running a real web server (nginx) and managing its whole lifecycle: start it, list it, read its logs, run a command inside it, then stop and remove it.

## What you'll build

Run and manage an nginx web server with docker run / ps / logs / exec / stop / rm.


---

## Step 1 — Run a web server in the background

`nginx` is a real, production web server. Start it detached (`-d`), give it a name, and publish its port 80 to port 8080 on the host:

```bash
docker run -d --name web -p 8080:80 nginx:latest
docker ps                      # the container is running
curl http://localhost:8080     # nginx serves its welcome page
```


---

## Step 2 — Inspect a running container

Read its logs, then run a command *inside* the container to see its hostname:

```bash
docker logs web
docker exec web cat /etc/hostname
docker exec -it web /bin/bash   # open an interactive shell, then 'exit'
```


---

## Step 3 — Stop, restart and clean up

```bash
docker stop web
docker ps -a                    # shows stopped containers too
docker start web
docker rm -f web                # force-remove (stops if running)
```

> **Note:** `docker ps` lists only **running** containers; `docker ps -a` lists **all** containers including stopped ones.


---

> ✅ **Test it:** Open http://localhost:8080 and confirm the nginx welcome page loads while the container is running, and that `docker ps` no longer lists `web` after `docker rm -f web`.
