from budget import estimate_tokens, budget
assert estimate_tokens("") == 0
assert estimate_tokens("abcd") == 1
assert estimate_tokens("abcde") == 2
parts = {"prompt": "x" * 2_000, "file_a": "y" * 80_000, "file_b": "z" * 40_000}   # 500 + 20000 + 10000 = 30500
assert budget(parts, 32_000, 4_000) == (30_500, 28_000, False)
assert budget(parts, 200_000, 4_000) == (30_500, 196_000, True)
print("budget: all checks passed")
