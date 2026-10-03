# Lab 15 — Deployments — Scaling & Self-Healing

**Folder:** `labs/lab15-deployments/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day2-02-k8s-deployments

## Goal

Run TaskBoard the production way — as a Deployment that keeps a desired number of replicas alive. You'll scale it, watch it self-heal when a Pod is deleted, and manage it both imperatively and from YAML.

## What you'll build

Create a Deployment, scale it, and watch Kubernetes self-heal a deleted Pod.


---

## Step 1 — Create and scale (imperative)

```bash
kubectl create deployment taskboard --image=nginx
kubectl get deployments
kubectl get pods
kubectl scale deployment taskboard --replicas=3
kubectl get pods               # now 3 Pods
```


---

## Step 2 — Watch it self-heal

Delete one Pod and watch the Deployment's ReplicaSet immediately create a replacement to restore the desired count:

```bash
kubectl get pods
kubectl delete pod <one-pod-name>
kubectl get pods               # a new Pod is already being created
```


---

## Step 3 — Declarative (deployment.yaml)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: taskboard
spec:
  replicas: 3
  selector:
    matchLabels:
      app: taskboard
  template:
    metadata:
      labels:
        app: taskboard
    spec:
      containers:
        - name: web
          image: nginx
          ports:
            - containerPort: 80
```

```bash
kubectl delete deployment taskboard
kubectl apply -f deployment.yaml
kubectl get pods
kubectl delete -f deployment.yaml
```

> **Note:** A Deployment manages a **ReplicaSet**, which guarantees the desired Pod count is always running — this is the self-healing that naked Pods (Lab 13) lack.


---

> ✅ **Test it:** After `kubectl delete pod <name>`, `kubectl get pods` still shows 3 Pods because the Deployment recreated the missing one automatically.
