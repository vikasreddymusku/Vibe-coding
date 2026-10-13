from average import average_of_top

assert average_of_top([10, 20, 30, 40], 2) == 35
assert average_of_top([5, 5], 5) == 5          # fewer scores than n is fine
try:
    average_of_top([], 3)
    print("no error for empty list")
except ZeroDivisionError:
    print("empty list -> ZeroDivisionError (the flaw)")
print("average: expected checks passed")
