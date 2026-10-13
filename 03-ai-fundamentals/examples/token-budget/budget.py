"""Estimate whether a prompt plus files fit in a context window.
The 4-characters-per-token rule is a rough English-text heuristic. Real counts depend on
the model's tokenizer, the language and the content (code and non-English text often use more)."""
import math

CHARS_PER_TOKEN = 4


def estimate_tokens(text):
    return math.ceil(len(text) / CHARS_PER_TOKEN)


def budget(parts, window, reserve_for_output):
    """parts: dict of name -> text. Returns (used, available_for_input, fits)."""
    used = sum(estimate_tokens(t) for t in parts.values())
    available = window - reserve_for_output
    return used, available, used <= available


if __name__ == "__main__":
    parts = {"prompt": "x" * 2_000, "file_a": "y" * 80_000, "file_b": "z" * 40_000}
    print(budget(parts, window=32_000, reserve_for_output=4_000))
    print(budget(parts, window=200_000, reserve_for_output=4_000))
