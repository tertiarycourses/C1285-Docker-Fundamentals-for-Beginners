"""
taskboard-cli — a tiny companion command-line tool for TaskBoard.

Used in Lab 05 to demonstrate CMD vs ENTRYPOINT: the image's ENTRYPOINT is
fixed to this tool, while CMD supplies the default sub-command, e.g.

    ENTRYPOINT ["python", "cli.py"]
    CMD ["list"]

So `docker run taskboard-cli` runs `list`, and
`docker run taskboard-cli add "Buy milk"` runs `add "Buy milk"`.

It reads/writes the same tasks.json that the web app uses (DATA_DIR).
"""
import os
import sys
import json

DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(__file__), "data"))


def _path():
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, "tasks.json")


def _load():
    try:
        with open(_path()) as fh:
            return json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def _save(tasks):
    with open(_path(), "w") as fh:
        json.dump(tasks, fh, indent=2)


def cmd_list(_args):
    tasks = _load()
    if not tasks:
        print("No tasks. Add one with:  add \"your task\"")
        return
    for t in tasks:
        mark = "x" if t.get("done") else " "
        print(f"[{mark}] {t['id']:>3}  {t['text']}")


def cmd_add(args):
    if not args:
        print("usage: add <task text>")
        sys.exit(2)
    tasks = _load()
    next_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": next_id, "text": " ".join(args), "done": False})
    _save(tasks)
    print(f"Added task #{next_id}: {' '.join(args)}")


def cmd_done(args):
    if not args:
        print("usage: done <id>")
        sys.exit(2)
    target = int(args[0])
    tasks = _load()
    for t in tasks:
        if t["id"] == target:
            t["done"] = True
    _save(tasks)
    print(f"Marked task #{target} done")


def cmd_clear(_args):
    _save([])
    print("Cleared all tasks")


COMMANDS = {"list": cmd_list, "add": cmd_add, "done": cmd_done, "clear": cmd_clear}


def main(argv):
    if not argv:
        argv = ["list"]
    name, rest = argv[0], argv[1:]
    handler = COMMANDS.get(name)
    if not handler:
        print(f"unknown command: {name}\navailable: {', '.join(COMMANDS)}")
        sys.exit(2)
    handler(rest)


if __name__ == "__main__":
    main(sys.argv[1:])
