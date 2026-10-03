# Labs — Docker Fundamentals for Beginners

Hands-on labs for the course **Docker Fundamentals for Beginners** (C1285). Every lab builds on the **TaskBoard** sample app in [`app/`](app/). Work through them in order.

## Morning — Docker

| Lab | Topic | What you build | Folder |
| --- | --- | --- | --- |
| [1](lab01-docker-commands/lab.md) | Docker commands | Run and manage an nginx web server with docker run / ps / logs / exec / stop / rm. | [lab01-docker-commands](lab01-docker-commands/) |
| [2](lab02-images-and-inspect/lab.md) | Docker commands | Pull images, copy a served file out of nginx with docker cp, and inspect a container. | [lab02-images-and-inspect](lab02-images-and-inspect/) |
| [3](lab03-build-image/lab.md) | Docker Build / Dockerfile | Write a Dockerfile for the TaskBoard Flask app, build it, and run the container. | [lab03-build-image](lab03-build-image/) |
| [4](lab04-dockerfile-best-practices/lab.md) | Dockerfile best practices | Add a .dockerignore and cache-friendly layer ordering to slim the TaskBoard build. | [lab04-dockerfile-best-practices](lab04-dockerfile-best-practices/) |
| [5](lab05-cmd-entrypoint/lab.md) | CMD vs ENTRYPOINT | Package taskboard-cli so ENTRYPOINT is fixed and CMD/args are overridable. | [lab05-cmd-entrypoint](lab05-cmd-entrypoint/) |
| [6](lab06-volumes/lab.md) | Volumes | Persist TaskBoard tasks in a named volume; live-edit host files via a bind mount. | [lab06-volumes](lab06-volumes/) |
| [7](lab07-networking/lab.md) | Networking | TaskBoard reaches Redis by DNS name on a custom network; publish ports to the host. | [lab07-networking](lab07-networking/) |
| [8](lab08-env-vars/lab.md) | Environment variables | Configure TaskBoard (APP_ENV, APP_TITLE) via ENV, -e and --env-file — no rebuild. | [lab08-env-vars](lab08-env-vars/) |
| [9](lab09-docker-hub/lab.md) | Docker Hub | Tag, push and pull the TaskBoard image via Docker Hub. | [lab09-docker-hub](lab09-docker-hub/) |
| [10](lab10-compose-single/lab.md) | Docker Compose | Define TaskBoard in docker-compose.yml; manage it with pull / up / ps / logs / down. | [lab10-compose-single](lab10-compose-single/) |
| [11](lab11-compose-redis/lab.md) | Docker Compose | Run TaskBoard + Redis with Compose; services find each other by name automatically. | [lab11-compose-redis](lab11-compose-redis/) |
| [12](lab12-compose-fullstack/lab.md) | Docker Compose | Run TaskBoard + Postgres + Redis with healthchecks and condition-based depends_on. | [lab12-compose-fullstack](lab12-compose-fullstack/) |

## Afternoon — Kubernetes

| Lab | Topic | What you build | Folder |
| --- | --- | --- | --- |
| [13](lab13-pods/lab.md) | Pods | Create, inspect and delete a Pod both imperatively and from a pod.yaml manifest. | [lab13-pods](lab13-pods/) |
| [14](lab14-namespaces/lab.md) | Namespaces | Create a dev namespace, run a Pod inside it, and list resources per namespace. | [lab14-namespaces](lab14-namespaces/) |
| [15](lab15-deployments/lab.md) | Deployments | Create a Deployment, scale it, and watch Kubernetes self-heal a deleted Pod. | [lab15-deployments](lab15-deployments/) |
| [16](lab16-rollouts/lab.md) | Rolling updates & rollbacks | Roll a Deployment forward to a new image with no downtime, then roll it back. | [lab16-rollouts](lab16-rollouts/) |
| [17](lab17-services/lab.md) | Services | Expose a Deployment with ClusterIP (internal) and NodePort (external) Services. | [lab17-services](lab17-services/) |
| [18](lab18-storage/lab.md) | Storage | Share data with emptyDir; provision durable storage with a PV + PVC. | [lab18-storage](lab18-storage/) |
| [19](lab19-jobs-cronjobs/lab.md) | Jobs & CronJobs | Run a batch Job (report) to completion and a scheduled CronJob (cleanup). | [lab19-jobs-cronjobs](lab19-jobs-cronjobs/) |
