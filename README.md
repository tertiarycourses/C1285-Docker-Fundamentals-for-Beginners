# Docker Fundamentals for Beginners

A one-day, hands-on course that takes one real application from a single Docker container to a multi-service Docker Compose stack and a scalable Kubernetes deployment.

| Course detail | Information |
|---|---|
| Course code | `C1285` |
| Programme | Non-WSQ |
| Duration | 1 day · 7.5 instructional hours (9:30am – 5:30pm) |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/docker-fundamentals-for-beginners.html) |

## About the course

Throughout the day you build and deploy **TaskBoard**, a Flask task tracker backed by Redis and PostgreSQL. In the morning you learn the Docker essentials: commands, Dockerfiles and the build cache, CMD vs ENTRYPOINT, volumes, networking, runtime configuration and Docker Hub. In the afternoon you define multi-service apps with Docker Compose. Then you move the app to Kubernetes, covering Pods, Namespaces, Deployments, rolling updates, Services, persistent storage, and Jobs and CronJobs. Every lab also runs in the browser on KillerCoda, so no local setup is required.

## Learning outcomes

By the end of the course you will be able to:

- Explain containerisation and the Docker architecture, and manage containers with the Docker CLI.
- Build custom images with a Dockerfile, applying layer caching and `.dockerignore` best practices.
- Distinguish CMD from ENTRYPOINT and package command-line tools correctly.
- Persist and share data using named volumes and bind mounts.
- Connect containers over a custom network using DNS, and publish services with port mapping.
- Configure containers at runtime with environment variables and publish images to Docker Hub.
- Define and run multi-service applications (web + cache + database) with Docker Compose.
- Explain Kubernetes architecture and deploy applications as Pods, Deployments and Services.
- Scale and self-heal workloads and perform zero-downtime rolling updates and rollbacks.
- Persist data with PersistentVolumes/Claims and run batch work with Jobs and CronJobs.

## Topics covered

- **Docker fundamentals:** containers vs virtual machines, Docker architecture, core commands
- **Dockerfile and build:** layers, build cache, `.dockerignore`, CMD vs ENTRYPOINT
- **Docker storage:** named volumes and bind mounts
- **Docker networking:** custom bridge networks, DNS and port mapping
- **Configuration and Docker Hub:** environment variables, tagging, pushing and pulling images
- **Docker Compose:** single-service, web + Redis, and full-stack web + PostgreSQL + Redis
- **Kubernetes fundamentals:** cluster architecture, Pods and Namespaces
- **Deployments and rollouts:** scaling, self-healing, rolling updates and rollbacks
- **Services:** ClusterIP and NodePort
- **Storage, Jobs and CronJobs:** emptyDir, PersistentVolumes and Claims, batch and scheduled work

## Labs

The shared TaskBoard app lives in [`labs/app/`](labs/app/). Each lab folder has a step-by-step `lab.md` plus its working files.

**Morning — Docker**

| Lab | What you build |
|---|---|
| [Lab 1 — Docker Commands](labs/lab01-docker-commands/) | Run and manage an nginx web server (run / ps / logs / exec / stop / rm) |
| [Lab 2 — Images & Inspecting Containers](labs/lab02-images-and-inspect/) | Pull images, `docker cp` a served file, inspect a container |
| [Lab 3 — Build the TaskBoard Image](labs/lab03-build-image/) | Write a Dockerfile and build the TaskBoard Flask image |
| [Lab 4 — Dockerfile Best Practices](labs/lab04-dockerfile-best-practices/) | `.dockerignore` and cache-friendly layer ordering |
| [Lab 5 — CMD vs ENTRYPOINT](labs/lab05-cmd-entrypoint/) | Package `taskboard-cli` with a fixed ENTRYPOINT and overridable CMD |
| [Lab 6 — Volumes](labs/lab06-volumes/) | Persist TaskBoard data with a named volume and a bind mount |
| [Lab 7 — Networking](labs/lab07-networking/) | TaskBoard ↔ Redis by DNS on a custom bridge network |
| [Lab 8 — Environment Variables](labs/lab08-env-vars/) | Configure TaskBoard via ENV, `-e` and `--env-file` |
| [Lab 9 — Docker Hub](labs/lab09-docker-hub/) | Tag, push and pull the TaskBoard image |

**Afternoon — Docker Compose and Kubernetes**

| Lab | What you build |
|---|---|
| [Lab 10 — Compose: Single Service](labs/lab10-compose-single/) | TaskBoard as a single Compose service |
| [Lab 11 — Compose: Web + Redis](labs/lab11-compose-redis/) | TaskBoard + Redis visit counter |
| [Lab 12 — Compose: Full Stack](labs/lab12-compose-fullstack/) | TaskBoard + PostgreSQL + Redis with healthchecks |
| [Lab 13 — Pods](labs/lab13-pods/) | Create and inspect Pods imperatively and declaratively |
| [Lab 14 — Namespaces](labs/lab14-namespaces/) | Isolate a `dev` environment |
| [Lab 15 — Deployments](labs/lab15-deployments/) | Scale and self-heal a Deployment |
| [Lab 16 — Rolling Updates & Rollbacks](labs/lab16-rollouts/) | Zero-downtime update, then roll back |
| [Lab 17 — Services](labs/lab17-services/) | ClusterIP (internal) and NodePort (external) |
| [Lab 18 — Storage](labs/lab18-storage/) | emptyDir and PersistentVolume / PVC |
| [Lab 19 — Jobs & CronJobs](labs/lab19-jobs-cronjobs/) | A batch Job and a scheduled CronJob |

## Courseware

| Item | Files |
|---|---|
| Slides | [PPTX](courseware/Docker-Fundamentals-for-Beginners-v1.pptx) · [PDF](courseware/Docker-Fundamentals-for-Beginners-v1.pdf) |
| Lesson Plan | [DOCX](courseware/LP-Docker-Fundamentals-for-Beginners.docx) · [PDF](courseware/LP-Docker-Fundamentals-for-Beginners.pdf) |
| Learner Guide | [DOCX](courseware/LG-Docker-Fundamentals-for-Beginners.docx) · [PDF](courseware/LG-Docker-Fundamentals-for-Beginners.pdf) · [Markdown](LG-Docker-Fundamentals-for-Beginners.md) |

The `build/` folder holds the scripts that produced this courseware.

## Getting started

```bash
cd labs/lab01-docker-commands
# follow lab.md, or open the KillerCoda link at the top of it to run in the browser
```

You need [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Docker Engine + Compose), [kubectl](https://kubernetes.io/docs/tasks/tools/) with a local cluster (minikube / kind) for the Kubernetes labs, or just KillerCoda in the browser. Lab 9 also needs a free [Docker Hub](https://hub.docker.com/) account.

## Distribution

This repository publishes the learner-facing courseware and labs. The course has no assessment.

---

© 2026 [Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/) · UEN 201200696W
