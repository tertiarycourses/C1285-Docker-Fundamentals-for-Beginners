# Lab 2 — Images & Inspecting Containers — pull, cp, inspect

**Folder:** `labs/lab02-images-and-inspect/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-01-docker-fundamentals

## Goal

Work with images and look inside containers. You will pull images, copy a file out of a running container with `docker cp`, and inspect container details.

## What you'll build

Pull images, copy a served file out of nginx with docker cp, and inspect a container.


---

## Step 1 — Work with images

```bash
docker pull nginx:latest
docker images                  # list local images
docker run -d --name web -p 8080:80 nginx:latest
```


---

## Step 2 — Copy a file out of the container (docker cp)

nginx serves `/usr/share/nginx/html/index.html`. Copy it to the host, edit it, and copy it back to change the live page — no rebuild needed:

```bash
docker cp web:/usr/share/nginx/html/index.html ./index.html
echo '<h1>Hello from TaskBoard class!</h1>' > index.html
docker cp ./index.html web:/usr/share/nginx/html/index.html
curl http://localhost:8080     # shows your new page
```


---

## Step 3 — Inspect the container

```bash
docker inspect web | grep -i ipaddress
docker stats --no-stream web   # CPU / memory snapshot
docker rm -f web
```

> **Note:** `docker cp` copies files between a container and the host in either direction — handy for grabbing logs or config out of a running container.


---

> ✅ **Test it:** After copying the edited file back, `curl http://localhost:8080` should show your custom heading instead of the default nginx page.
