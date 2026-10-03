"""Retitle/recode the labs tree and the LG Markdown mirror for C1285 (one-day course)."""
from pathlib import Path

OLD_REPO = "https://github.com/tertiarycourses/TGS-2021010366-Application-Integration-with-Docker-and-Kubernetes"
NEW_REPO = "https://github.com/tertiarycourses/C1285-Docker-Fundamentals-for-Beginners"
COMMON = [
    (OLD_REPO, NEW_REPO),
    ("Application Integration with Docker and Kubernetes", "Docker Fundamentals for Beginners"),
    (" (and in Kubernetes, with ConfigMaps and Secrets — Day 2).", " (and in Kubernetes, with ConfigMaps and Secrets)."),
    ("how Kubernetes gets your app on Day 2:", "how Kubernetes gets your app this afternoon:"),
    ("deploy to Kubernetes on Day 2.", "deploy to Kubernetes later today."),
    ("On Day 2 you'll deploy", "Later today you'll deploy"),
]


def patch(path, subs):
    p = Path(path)
    s = p.read_text()
    for a, b in subs:
        s = s.replace(a, b)
    p.write_text(s)


for md in Path("labs").rglob("*.md"):
    patch(md, COMMON)

readme = Path("labs/README.md").read_text()
readme = readme.replace("Hands-on labs for WSQ course **TGS-2021010366**.", "Hands-on labs for the course **Docker Fundamentals for Beginners** (C1285).")
readme = readme.replace("## Day 1 — Docker", "## Morning — Docker")
readme = readme.replace("## Day 2 — Kubernetes", "## Afternoon — Kubernetes")
readme = readme.split("\n## Assessments")[0].rstrip() + "\n"
Path("labs/README.md").write_text(readme)

src = Path("source-wsq/LG-Application-Integration-with-Docker-and-Kubernetes.md").read_text()
for a, b in COMMON + [
    ("**Course Code:** TGS-2021010366", "**Course Code:** C1285"),
    ("| 1.0 | 30 June 2026 | First version — step-by-step guide to all 19 Docker & Kubernetes labs, built around the TaskBoard sample app; MD and DOCX generated from one source |",
     "| 1.0 | 3 October 2026 | First version — step-by-step guide to all 19 Docker & Kubernetes labs for the one-day course. |"),
    ("in the WSQ course ", "in the course "),
    ("(Course Code: TGS-2021010366)", "(Course Code: C1285)"),
    ("Over two days you build", "Over one day you build"),
    ("**Day 1 (Docker):**", "**Morning (Docker):**"),
    ("Docker Hub, Docker Compose (Labs 1–12).", "Docker Hub (Labs 1–9)."),
    ("**Day 2 (Kubernetes):**", "**Afternoon (Docker Compose & Kubernetes):** Docker Compose (Labs 10–12),"),
    ("(all Day 1 labs)", "(all Docker labs)"),
    ("All Day 2 Kubernetes labs", "All Kubernetes labs"),
    ("built-in Kubernetes) for Day 2.", "built-in Kubernetes) for the Kubernetes labs."),
]:
    assert a in src or a in (OLD_REPO,) or "Day 2" in a, a
    src = src.replace(a, b)
Path("LG-Docker-Fundamentals-for-Beginners.md").write_text(src)
print("ok")
