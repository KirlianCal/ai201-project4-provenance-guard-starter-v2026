"""
What my test runs. Unit 8, Milestone 3.

Criterion numbers match criteria.md:
  1 own writing rarely flagged    2 AI and human text score far apart
  3 all three labels reachable    4 appeals    5 bad input

Every request body carries its own creator_id, so my 5-per-minute limit never
interferes with the eval itself. Criterion 4 needs a submission followed by an
appeal, which this file cannot express, so appeal_eval.py runs it instead.
"""

from pathlib import Path

ROOT = Path(__file__).parent


def _bodies(folder):
    out = []
    for path in sorted((ROOT / "samples" / folder).glob("*.txt")):
        text = path.read_text(encoding="utf-8").strip()
        out.append({"text": text, "creator_id": f"eval-{path.stem}"})
    return out


SCENARIOS = [
    {
        "name": "own writing (12 pieces)",
        "criterion": 1,
        "bodies": _bodies("own"),
    },
    {
        "name": "clearly human (6 book excerpts)",
        "criterion": 2,
        "bodies": _bodies("human"),
    },
    {
        "name": "clearly AI (6 Claude paragraphs)",
        "criterion": 2,
        "bodies": _bodies("ai"),
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "bodies": [
            {"text": "The labyrinthine bureaucracy, ostensibly designed to expedite grievances, instead metastasized into an inscrutable apparatus.",
             "creator_id": "eval-label-human"},
            {"text": "We walked to the park after school and talked about the game.",
             "creator_id": "eval-label-unsure"},
            {"text": "The cat sat on the mat. The dog sat on the mat. The cat sat on the rug. The dog sat on the rug.",
             "creator_id": "eval-label-ai"},
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval-bad-empty"},
            {"text": "   ", "creator_id": "eval-bad-whitespace"},
            {"creator_id": "eval-bad-missing-text"},
            {"text": None, "creator_id": "eval-bad-null"},
            {"text": 12345, "creator_id": "eval-bad-number"},
            {"text": ["a", "b"], "creator_id": "eval-bad-list"},
            {"text": "hi", "creator_id": "eval-bad-short"},
            {"text": "We walked to the park after school and talked about the game."},  # no creator_id
            {"text": "word " * 360, "creator_id": "eval-bad-1800"},
            {"text": "word " * 360 + "x", "creator_id": "eval-bad-1801"},
            {"text": "word " * 50000, "creator_id": "eval-bad-huge"},
            {"text": "... !!! ??? ,,, ;;;", "creator_id": "eval-bad-punct"},
        ],
    },
]


def validate() -> list[str]:
    """Complain about anything malformed before a long run, not during it."""
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")
        bodies = scenario.get("bodies")
        if not bodies:
            problems.append(f"scenario {i} has no bodies")
            continue
        for j, body in enumerate(bodies, 1):
            if not isinstance(body, dict):
                problems.append(f"scenario {i}, body {j} is not a dict")
    return problems