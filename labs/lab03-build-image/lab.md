# Lab 3 — Build the TaskBoard Image with a Dockerfile

**Folder:** `labs/lab03-build-image/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-01-docker-fundamentals

## Goal

Package a real application — the TaskBoard Flask web app — into your own Docker image using a Dockerfile, then run it as a container. This image is reused by several later labs.

## What you'll build

Write a Dockerfile for the TaskBoard Flask app, build it, and run the container.


---

## Step 1 — What's in the folder

`app.py` (the TaskBoard Flask app), `templates/index.html` (the board UI), `requirements.txt`, and a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Each line is a cached image **layer**. Notice `requirements.txt` is copied and installed *before* the app code, so editing `app.py` doesn't re-run `pip install`.


---

## Step 2 — Build the image

```bash
docker build -t taskboard:1.0 .
docker images | grep taskboard
```


---

## Step 3 — Run the container

```bash
docker run -d --name taskboard -p 8080:5000 taskboard:1.0
curl http://localhost:8080/health
# open http://localhost:8080 and add a few tasks
```


---

## Step 4 — Watch the build cache

Edit `app.py` (e.g. change `APP_TITLE` default) and rebuild — only the layers from `COPY . .` onward rebuild; the `pip install` layer is reused from cache:

```bash
docker build -t taskboard:1.0 .
docker rm -f taskboard
```

> **Note:** Tag images with a name **and** version (`taskboard:1.0`) so you can roll forward/back later — exactly what you'll do in the Kubernetes rollout lab.


---

> ✅ **Test it:** `curl http://localhost:8080/health` returns `{"status": "ok", ...}` and the board at http://localhost:8080 lets you add a task that appears in the list.
