"""Criterion 4: appeals. Needs a real submission first, so it cannot live in scenarios.py."""
import json
import urllib.error
import urllib.request

BASE = "http://127.0.0.1:5000"
TEXT = "We walked to the park after school and talked about the game."


def post(path, body):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(BASE + path, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        try:
            return err.code, json.loads(err.read().decode("utf-8"))
        except Exception:
            return err.code, None


def get_log():
    with urllib.request.urlopen(BASE + "/log") as resp:
        return json.loads(resp.read().decode("utf-8"))["entries"]


def entries_for(cid):
    return [e for e in get_log() if e.get("content_id") == cid]


def run_trial(n):
    appeals_ok, ids = 0, []
    for i in range(1, 9):
        _, body = post("/submit", {"text": TEXT, "creator_id": f"eval-appeal-t{n}-{i}"})
        cid = body.get("content_id") if body else None
        ids.append(cid)
        if not cid:
            continue
        before = [e for e in entries_for(cid) if e.get("status") == "decided"]
        status, resp = post("/appeal", {"content_id": cid, "reasoning": "I wrote this myself."})
        after = entries_for(cid)
        appeals = [e for e in after if e.get("event") == "appeal"]
        decided = [e for e in after if e.get("status") == "decided"]
        if (status == 200 and resp and resp.get("status") == "under_review"
                and len(appeals) == 1 and before and decided == before):
            appeals_ok += 1

    errors_ok = 0
    checks = [
        ({"content_id": "does-not-exist", "reasoning": "x"}, 404, "unknown_content_id"),
        ({"reasoning": "x"}, 400, "missing_content_id"),
        ({"content_id": ids[0], "reasoning": ""}, 400, "missing_reasoning"),
    ]
    for body, want_status, want_error in checks:
        status, resp = post("/appeal", body)
        if status == want_status and resp and resp.get("error") == want_error:
            errors_ok += 1

    status, _ = post("/appeal", {"content_id": ids[0], "reasoning": "Second appeal."})
    repeat_ok = status == 200 and len([e for e in entries_for(ids[0]) if e.get("event") == "appeal"]) == 2

    print(f"Trial {n}: appeals {appeals_ok}/8, error cases {errors_ok}/3, repeat appeal {'1' if repeat_ok else '0'}/1")


if __name__ == "__main__":
    for n in (1, 2, 3):
        run_trial(n)