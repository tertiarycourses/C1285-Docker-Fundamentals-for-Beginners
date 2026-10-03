# Lab 19 — Jobs & CronJobs — Batch and Scheduled Tasks

**Folder:** `labs/lab19-jobs-cronjobs/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day2-05-k8s-storage-jobs

## Goal

Run work that finishes (unlike a web server that runs forever). A Job runs Pods to completion — perfect for a TaskBoard report — and a CronJob runs Jobs on a schedule, perfect for a nightly cleanup.

## What you'll build

Run a batch Job (report) to completion and a scheduled CronJob (cleanup).


---

## Step 1 — Job (run to completion)

```bash
kubectl create job hello --image=busybox -- echo 'Hello from a Job!'
kubectl get jobs
kubectl logs job/hello
kubectl delete job hello
```

Declarative — 3 completions, 2 running in parallel:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: taskboard-report
spec:
  completions: 3
  parallelism: 2
  template:
    spec:
      restartPolicy: Never
      containers:
        - name: report
          image: busybox
          command: ["sh", "-c", "echo 'Generating TaskBoard report...'; sleep 5; echo done"]
```

```bash
kubectl apply -f job.yaml
kubectl get pods                 # up to 2 running at once
kubectl get job taskboard-report # COMPLETIONS climbs to 3/3
kubectl delete -f job.yaml
```


---

## Step 2 — CronJob (scheduled)

```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: taskboard-cleanup
spec:
  schedule: "*/1 * * * *"     # every minute (demo); real cleanup might be nightly
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: Never
          containers:
            - name: cleanup
              image: busybox
              command: ["sh", "-c", "echo 'Cleaning up old TaskBoard sessions...'; date"]
```

```bash
kubectl apply -f cronjob.yaml
kubectl get cronjob taskboard-cleanup
# wait ~1 minute for the first Job to be created:
kubectl get jobs
kubectl logs job/<created-job-name>
kubectl delete -f cronjob.yaml
```

> **Note:** Jobs use `restartPolicy: Never` and do **not** restart after success — unlike a Deployment, which keeps Pods running forever. CronJobs use standard cron syntax.


---

> ✅ **Test it:** `kubectl get job taskboard-report` reaches `3/3` completions, and after ~1 minute the CronJob has spawned at least one Job visible in `kubectl get jobs`.
