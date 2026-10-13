"""A toy next-word predictor. Real language models are vastly larger and use neural networks,
but the task is the same: given the words so far, choose a likely next word."""
import random
from collections import Counter, defaultdict

TEXT = ("the cat sat on the mat . the cat ate the fish . "
        "the dog sat on the rug . the dog ate the bone .")


def train(text):
    words = text.split()
    follows = defaultdict(Counter)
    for current, nxt in zip(words, words[1:]):
        follows[current][nxt] += 1      # count what follows each word
    return follows


def next_word_probabilities(model, word):
    counts = model[word]
    total = sum(counts.values())
    return {w: c / total for w, c in counts.items()}


def generate(model, start, length, seed):
    rng = random.Random(seed)           # a seed makes the "randomness" repeatable
    out = [start]
    for _ in range(length):
        probs = next_word_probabilities(model, out[-1])
        if not probs:
            break
        words, weights = zip(*probs.items())
        out.append(rng.choices(words, weights=weights)[0])
    return " ".join(out)


if __name__ == "__main__":
    model = train(TEXT)
    print(next_word_probabilities(model, "the"))
    print(generate(model, "the", 8, seed=1))
    print(generate(model, "the", 8, seed=2))
