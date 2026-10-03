# Lab 4 — Dockerfile Best Practices — .dockerignore & layer caching

**Folder:** `labs/lab04-dockerfile-best-practices/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-01-docker-fundamentals

## Goal

Make the TaskBoard image smaller and faster to build. You'll add a `.dockerignore`, order instructions for maximum cache reuse, and compare image sizes.

## What you'll build

Add a .dockerignore and cache-friendly layer ordering to slim the TaskBoard build.


---

## Step 1 — Why .dockerignore

`COPY . .` copies everything in the folder into the image — including `.git/`, caches and local `data/`. A `.dockerignore` keeps them out, shrinking the image and the build context:

```bash
__pycache__/
*.pyc
data/
.git/
.env
*.md
```


---

## Step 2 — Cache-friendly ordering

Dependencies change rarely; source changes often. Copy and install `requirements.txt` **before** copying the source so the dependency layer is cached across code edits (this is already done in our Dockerfile):

```bash
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```


---

## Step 3 — Build and compare

```bash
docker build -t taskboard:slim .
docker images taskboard
# edit app.py, rebuild, and watch most layers say 'CACHED'
docker build -t taskboard:slim .
```

> **Note:** `python:3.11-slim` is already a smaller base than `python:3.11`. For even smaller images, multi-stage builds copy only the artifacts you need into a fresh final stage.


---

> ✅ **Test it:** The second `docker build` completes in seconds with most steps showing `CACHED`, and `docker images taskboard` shows the image built from the slim base.
