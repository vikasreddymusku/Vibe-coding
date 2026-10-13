from toy_model import TEXT, train, next_word_probabilities, generate
m = train(TEXT)
p = next_word_probabilities(m, "the")
assert abs(sum(p.values()) - 1) < 1e-9
assert p["cat"] == 0.25 and p["dog"] == 0.25 and p["mat"] == 0.125   # "the" appears 8 times
assert next_word_probabilities(m, "sat") == {"on": 1.0}              # always followed by "on"
assert generate(m, "the", 8, seed=1) == generate(m, "the", 8, seed=1)  # same seed, same text
assert generate(m, "the", 8, seed=1) != generate(m, "the", 8, seed=2)  # different seed, different text
print("toy_model: all checks passed")
