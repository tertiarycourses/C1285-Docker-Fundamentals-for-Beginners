# Lab 5 — CMD vs ENTRYPOINT — the taskboard-cli tool

**Folder:** `labs/lab05-cmd-entrypoint/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day1-01-docker-fundamentals

## Goal

Understand the difference between CMD and ENTRYPOINT by packaging a real command-line tool — `taskboard-cli` — that lists and adds tasks. ENTRYPOINT fixes the program; CMD supplies the default arguments you can override at runtime.

## What you'll build

Package taskboard-cli so ENTRYPOINT is fixed and CMD/args are overridable.


---

## Step 1 — The Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY cli.py .
# ENTRYPOINT fixes the executable; CMD is the default argument (overridable).
ENTRYPOINT ["python", "cli.py"]
CMD ["list"]
```

`ENTRYPOINT` is the executable that always runs. `CMD` is the **default argument** — here `list` — which is replaced by anything you pass on `docker run`.


---

## Step 2 — Build it

```bash
docker build -t taskboard-cli .
```


---

## Step 3 — CMD is the default; run args override it

```bash
docker run --rm taskboard-cli                 # runs the default: list
docker run --rm taskboard-cli add "Buy milk"   # overrides CMD with: add ...
docker run --rm taskboard-cli add "Ship release"
docker run --rm taskboard-cli list
```


---

## Step 4 — ENTRYPOINT vs CMD — the contrast

|  | CMD only | ENTRYPOINT + CMD |
| --- | --- | --- |
| Dockerfile | CMD ["python","cli.py","list"] | ENTRYPOINT ["python","cli.py"]<br>CMD ["list"] |
| `docker run img` | runs list | runs list |
| `docker run img add x` | tries to run `add` as a command (error) | runs `cli.py add x` ✔ |

> **Note:** Use **ENTRYPOINT** when the image *is* a specific tool and arguments vary (like our CLI). Use **CMD** alone when you want an easily replaceable default command. Both use the JSON *exec form* `["a","b"]` to avoid an extra shell.


---

> ✅ **Test it:** `docker run --rm taskboard-cli` prints the task list, and `docker run --rm taskboard-cli add "Demo"` adds a task — the same image, different CMD arguments.
