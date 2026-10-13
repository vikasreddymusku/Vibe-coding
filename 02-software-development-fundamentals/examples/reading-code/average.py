"""A short function with a flaw for you to find by reading, before you run the tests."""


def average_of_top(scores, n):
    """Average of the n highest scores."""
    ordered = sorted(scores, reverse=True)
    top = ordered[:n]
    return sum(top) / len(top)
