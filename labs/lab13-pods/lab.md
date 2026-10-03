# Lab 13 — Kubernetes Pods — Imperative & Declarative

**Folder:** `labs/lab13-pods/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day2-01-k8s-pods-namespaces

## Goal

Meet the smallest deployable unit in Kubernetes — the Pod. You'll create one imperatively with a single command, inspect it, then create one declaratively from a YAML file (the approach you'll use for everything afterwards).

## What you'll build

Create, inspect and delete a Pod both imperatively and from a pod.yaml manifest.


---

## Step 1 — Imperative (one command)

```bash
kubectl run web --image=nginx
kubectl get pods
kubectl get pods -o wide          # node + Pod IP
kubectl describe pod web          # events, container, volumes
```

Look inside the Pod, then remove it:

```bash
kubectl logs web
kubectl exec web -- cat /etc/hostname
kubectl exec -it web -- /bin/sh   # interactive shell, then 'exit'
kubectl delete pod web
```


---

## Step 2 — Declarative (pod.yaml)

Real work is declarative: you describe the desired state in YAML and apply it.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: taskboard
  labels:
    app: taskboard
spec:
  containers:
    - name: web
      image: nginx          # swap for <user>/taskboard:1.0 to run your own image
      ports:
        - containerPort: 80
```

```bash
kubectl apply -f pod.yaml
kubectl get pods
kubectl describe pod taskboard
kubectl delete -f pod.yaml
```

> **Note:** Pods are **ephemeral** — if a Pod dies it is not recreated. That's why you almost always run Pods through a **Deployment** (Lab 15), not on their own.


---

> ✅ **Test it:** `kubectl get pods` shows the `taskboard` Pod as `Running` after `kubectl apply`, and it disappears after `kubectl delete -f pod.yaml`.
