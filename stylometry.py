"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """Coefficient of variation of sentence length (stdev / mean). Higher = more human.
    Fewer than two sentences has no spread, so it returns 0.0 (style_signal treats that as neutral)."""
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean if mean else 0.0


def type_token_ratio(text: str) -> float:
    """Unique words / total words, over the first 100 words so length matters less. Higher = more human."""
    w = words(text)[:100]
    return len(set(w)) / len(w) if w else 0.0


def punctuation_density(text: str) -> float:
    """Commas, semicolons, colons, dashes, brackets and quotes per word. Hypothesis: higher = more human."""
    w = words(text)
    if not w:
        return 0.0
    marks = re.findall(r'[,;:—–()"“”]|--| - ', text)
    return len(marks) / len(w)


def _clamp(x: float) -> float:
    return max(0.0, min(1.0, x))


def style_signal(text: str) -> float:
    """0-1 score, higher = more likely AI. Each measure is flipped and scaled to 0-1 first."""
    import config

    n_sentences = len([s for s in sentences(text) if words(s)])
    # Scale cutoffs are first guesses; adjust only on fresh text, never on the 24 committed samples.
    spread_ai = 0.5 if n_sentences < 2 else 1 - _clamp(sentence_length_spread(text) / 0.7)
    vocab_ai = _clamp((0.85 - type_token_ratio(text)) / 0.30)
    punct_ai = 1 - _clamp(punctuation_density(text) / 0.12)

    score = (
        config.STYLE_WEIGHT_SPREAD * spread_ai
        + config.STYLE_WEIGHT_VOCAB * vocab_ai
        + config.STYLE_WEIGHT_PUNCT * punct_ai
    )
    return round(_clamp(score), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
