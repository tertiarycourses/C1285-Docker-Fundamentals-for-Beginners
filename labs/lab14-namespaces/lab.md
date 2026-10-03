# Lab 14 — Kubernetes Namespaces — Environment Isolation

**Folder:** `labs/lab14-namespaces/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day2-01-k8s-pods-namespaces

## Goal

Use namespaces to keep environments apart inside one cluster. You'll create a `dev` namespace, run a Pod in it, and see how resources are isolated by namespace.

## What you'll build

Create a dev namespace, run a Pod inside it, and list resources per namespace.


---

## Step 1 — List and create namespaces

```bash
kubectl get namespaces
kubectl create namespace dev
```


---

## Step 2 — Run a Pod inside a namespace

```bash
kubectl run web --image=nginx -n dev
kubectl get pods -n dev
kubectl get pods                  # default ns: not shown here
kubectl get pods --all-namespaces
```


---

## Step 3 — Clean up the whole namespace

Deleting a namespace removes **everything** inside it — a fast way to tear down an environment:

```bash
kubectl delete namespace dev
```

> **Note:** Namespaces are perfect for separating `dev` / `staging` / `prod` (or per-team quotas) on a single shared cluster.


---

> ✅ **Test it:** `kubectl get pods -n dev` lists the Pod while it exists, and `kubectl delete namespace dev` removes the namespace and its Pod together.
