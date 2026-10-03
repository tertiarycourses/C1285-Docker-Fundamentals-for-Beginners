# Lab 9 — Sharing Images — Push to Docker Hub

**Folder:** `labs/lab09-docker-hub/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-01-docker-fundamentals

## Goal

Publish your TaskBoard image to Docker Hub so anyone (and any Kubernetes cluster) can pull and run it. You'll log in, tag the image under your account, push it, then pull and run it as if you were a new user.

## What you'll build

Tag, push and pull the TaskBoard image via Docker Hub.


---

## Step 1 — Registry vs repository

A **registry** (Docker Hub) hosts **repositories**; each repository holds the tagged versions of one image. Public images like `nginx` and `redis` live there too.


---

## Step 2 — Log in and tag

Replace `<user>` with your Docker Hub username:

```bash
docker login
docker tag taskboard:1.0 <user>/taskboard:1.0
```


---

## Step 3 — Push

```bash
docker push <user>/taskboard:1.0
# browse to https://hub.docker.com/r/<user>/taskboard to see it
```


---

## Step 4 — Pull & run as a new user

```bash
docker rmi <user>/taskboard:1.0          # remove the local copy
docker run -d --name tb -p 8080:5000 <user>/taskboard:1.0
curl http://localhost:8080/health
docker rm -f tb
docker logout
```

> **Note:** This is exactly how Kubernetes gets your app this afternoon: the cluster pulls your image from a registry by `name:tag`. Always push a versioned tag, not just `latest`.


---

> ✅ **Test it:** Your image appears at hub.docker.com under `<user>/taskboard`, and after removing the local image you can `docker run` it straight from the registry.
