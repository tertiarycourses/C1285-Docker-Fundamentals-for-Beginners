# Lab 18 — Kubernetes Storage — emptyDir, PV & PVC

**Folder:** `labs/lab18-storage/`  ·  **KillerCoda:** https://killercoda.com/tertiary-labs/course/killercoda/day2-05-k8s-storage-jobs

## Goal

Persist data in Kubernetes. You'll share a scratch directory between two containers with `emptyDir`, then provision durable storage with a PersistentVolume and claim it with a PersistentVolumeClaim so data survives Pod deletion.

## What you'll build

Share data with emptyDir; provision durable storage with a PV + PVC.


---

## Step 1 — emptyDir (shared, temporary)

`emptyDir` is a scratch volume shared by all containers in a Pod and deleted with the Pod. Here a `writer` container writes a file a `reader` container reads:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: shared-pod
spec:
  containers:
    - name: writer
      image: busybox
      command: ["sh", "-c", "echo 'hello from writer' > /data/message.txt && sleep 3600"]
      volumeMounts:
        - name: shared-data
          mountPath: /data
    - name: reader
      image: busybox
      command: ["sh", "-c", "sleep 5 && cat /data/message.txt && sleep 3600"]
      volumeMounts:
        - name: shared-data
          mountPath: /data
  volumes:
    - name: shared-data
      emptyDir: {}
```

```bash
kubectl apply -f emptydir-pod.yaml
kubectl exec shared-pod -c reader -- cat /data/message.txt
kubectl delete pod shared-pod      # emptyDir data is gone
```


---

## Step 2 — PersistentVolume & Claim (durable)

A PV is cluster storage; a PVC requests a slice of it. Bind them, then mount the claim in a Pod:

```bash
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
kubectl get pv,pvc                 # both should show Bound
```

```bash
kubectl apply -f pod-with-pvc.yaml
kubectl exec pvc-pod -- cat /data/file.txt
kubectl delete pod pvc-pod
kubectl apply -f pod-with-pvc.yaml # recreate...
kubectl exec pvc-pod -- cat /data/file.txt   # ...data is still there
kubectl delete pod pvc-pod
kubectl delete -f pvc.yaml -f pv.yaml
```

> **Note:** This PV/PVC pattern is how a real TaskBoard Postgres database keeps its data in Kubernetes — storage outlives any individual Pod.


---

> ✅ **Test it:** After deleting and recreating `pvc-pod`, `kubectl exec pvc-pod -- cat /data/file.txt` still prints `persistent data` — the PVC kept it across Pod deletion.
