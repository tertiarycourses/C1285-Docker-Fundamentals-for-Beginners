# Lab 16 — Rolling Updates & Rollbacks

**Folder:** `labs/lab16-rollouts/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day2-03-k8s-rollouts

## Goal

Ship a new version of TaskBoard with zero downtime, then instantly roll back when something's wrong. You'll update the container image, track the rollout, and revert to a previous revision.

## What you'll build

Roll a Deployment forward to a new image with no downtime, then roll it back.


---

## Step 1 — Deploy v1, then update the image

```bash
kubectl create deployment taskboard --image=nginx:1.24 --replicas=3
kubectl rollout status deployment taskboard
kubectl describe deployment taskboard | grep Image
```

Update the image — Kubernetes shifts Pods gradually from the old to the new ReplicaSet (rolling update, the default strategy):

```bash
kubectl set image deployment/taskboard nginx=nginx:1.25
kubectl rollout status deployment taskboard
kubectl describe deployment taskboard | grep Image   # now 1.25
```


---

## Step 2 — Roll back

```bash
kubectl rollout history deployment taskboard
kubectl rollout undo deployment taskboard            # back to 1.24
kubectl describe deployment taskboard | grep Image
kubectl rollout undo deployment taskboard --to-revision=2   # forward to 1.25 again
kubectl delete deployment taskboard
```

> **Note:** Rolling updates keep old and new Pods running simultaneously so users never see downtime; a rollback is just a rollout to a previous revision.


---

> ✅ **Test it:** `kubectl describe deployment taskboard | grep Image` shows `nginx:1.25` after the update and `nginx:1.24` after `kubectl rollout undo`.
