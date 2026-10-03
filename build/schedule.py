"""One-day C1285 schedule: every WSQ teaching row (both days) rescaled onto 450 min.

Dropped (day-structure / WSQ only): both tea breaks x2 days, the 2nd lunch, Day-1 recap (5),
Day-2 recap & objectives (15), both 'Morning Q&A' (15+15), Final Assessment (75).
Kept: welcome + closing (feedback without TRAQOM). One 30-min lunch at 1:00pm.
"""
WSQ = [  # (label, WSQ minutes)
    ("Welcome, course objectives & overview", 15),
    ("Topic 1: Containers, Docker architecture & core concepts", 30),
    ("Lab 1: Docker Commands — Run & Manage Containers", 25),
    ("Lab 2: Images & Inspecting Containers — pull, cp, inspect", 25),
    ("Topic 2: Building images — Dockerfile, layers & build cache", 20),
    ("Lab 3: Build the TaskBoard Image with a Dockerfile", 35),
    ("Lab 4: Dockerfile Best Practices — .dockerignore & layer caching", 25),
    ("Lab 5: CMD vs ENTRYPOINT — the taskboard-cli tool", 35),
    ("Topic 3: Docker storage — volumes & bind mounts", 20),
    ("Lab 6: Docker Storage — Named Volumes & Bind Mounts", 30),
    ("Topic 4: Docker networking — bridges, DNS & ports", 20),
    ("Lab 7: Docker Networking — Custom Bridge, DNS & Port Mapping", 30),
    ("Lab 8: Configuration with Environment Variables", 20),
    ("Lab 9: Sharing Images — Push to Docker Hub", 20),
    ("Topic 5: Docker Compose — multi-service apps", 15),
    ("Lab 10: Docker Compose — Single Service", 20),
    ("Lab 11: Docker Compose — Multi-Service (Web + Redis)", 20),
    ("Lab 12: Docker Compose — Full-Stack (Web + PostgreSQL + Redis)", 25),
    ("Topic 6: Kubernetes architecture & kubectl", 40),
    ("Lab 13: Kubernetes Pods — Imperative & Declarative", 35),
    ("Lab 14: Kubernetes Namespaces — Environment Isolation", 25),
    ("Topic 7: Deployments, ReplicaSets & self-healing", 20),
    ("Lab 15: Deployments — Scaling & Self-Healing", 40),
    ("Lab 16: Rolling Updates & Rollbacks", 35),
    ("Topic 8: Services & networking in Kubernetes", 20),
    ("Lab 17: Services — ClusterIP & NodePort", 35),
    ("Topic 9: Storage, Jobs & CronJobs", 15),
    ("Lab 18: Kubernetes Storage — emptyDir, PV & PVC", 25),
    ("Lab 19: Jobs & CronJobs — Batch and Scheduled Tasks", 25),
    ("Course review, learner feedback & closing", 30),
]
tot = sum(m for _, m in WSQ)
# Largest-remainder rounding in 5-min units so the drift is spread, not dumped on one row.
exact = [m / tot * 90 for _, m in WSQ]          # 90 units x 5 min = 450 min
units = [int(e) for e in exact]
for i in sorted(range(len(exact)), key=lambda i: exact[i] - units[i], reverse=True)[:90 - sum(units)]:
    units[i] += 1
mins = [u * 5 for u in units]
assert sum(mins) == 450 and min(mins) >= 5
# One 30-min lunch after Lab 9 (before Topic 5, Docker Compose).
cut = next(i for i, (l, _) in enumerate(WSQ) if l.startswith("Topic 5"))
ROWS = list(zip([l for l, _ in WSQ], mins))

def fmt(t):
    h, m = divmod(t, 60)
    return f"{(h - 1) % 12 + 1}:{m:02d}"

if __name__ == "__main__":
    print("WSQ teaching total", tot, "-> scale", 450 / tot)
    t = 570
    for i, (l, m) in enumerate(ROWS):
        if i == cut:
            print(f"{fmt(t)} – {fmt(t+30)}   30  Lunch"); t += 30
        print(f"{fmt(t)} – {fmt(t+m)}  {m:3d}  {l}")
        t += m
    assert t == 17 * 60 + 30, t
