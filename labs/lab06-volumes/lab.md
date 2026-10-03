# Lab 6 — Docker Storage — Named Volumes & Bind Mounts

**Folder:** `labs/lab06-volumes/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-02-docker-storage

## Goal

Make TaskBoard's data survive container removal. You'll persist its tasks.json in a **named volume**, prove the data outlives the container, then use a **bind mount** to edit files on the host and see them live in the container.

## What you'll build

Persist TaskBoard tasks in a named volume; live-edit host files via a bind mount.


---

## Step 1 — The problem: container data is ephemeral

By default everything written inside a container lives in its writable layer and is **lost** when the container is removed. TaskBoard writes its tasks to `DATA_DIR` — point that at a mounted volume and the data persists.


---

## Step 2 — Named volume (persistent app data)

```bash
docker volume create taskboard-data
docker run -d --name tb -p 8080:5000 \
  -e DATA_DIR=/data -v taskboard-data:/data taskboard:1.0
# add a few tasks at http://localhost:8080, then:
docker rm -f tb
```

Start a **brand-new** container on the **same volume** — your tasks are still there:

```bash
docker run -d --name tb2 -p 8080:5000 \
  -e DATA_DIR=/data -v taskboard-data:/data taskboard:1.0
curl http://localhost:8080/api/tasks   # the tasks you added are back
docker rm -f tb2
```


---

## Step 3 — Bind mount (live host files)

A bind mount maps a host folder straight into the container. Edit on the host, see it instantly inside — great for development:

```bash
mkdir -p data && echo '[]' > data/tasks.json
docker run -d --name tb3 -p 8080:5000 \
  -e DATA_DIR=/data -v $(pwd)/data:/data taskboard:1.0
# add tasks in the browser, then read them straight off the host:
cat data/tasks.json
docker rm -f tb3
```

|  | Named volume | Bind mount |
| --- | --- | --- |
| Syntax | -v taskboard-data:/data | -v $(pwd)/data:/data |
| Managed by | Docker | You (host path) |
| Best for | production data, databases | local development, live edits |

> **Note:** Named volumes are stored under Docker (`/var/lib/docker/volumes`) and are the right choice for databases; bind mounts tie you to an exact host path but are perfect for editing code live.


---

> ✅ **Test it:** After removing `tb` and starting `tb2` on the same named volume, `curl http://localhost:8080/api/tasks` returns the tasks you added earlier — they survived container deletion.
