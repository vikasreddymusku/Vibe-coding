from memory_estimate import weight_gigabytes
assert weight_gigabytes(7, "16-bit") == 14.0
assert weight_gigabytes(7, "4-bit") == 3.5
assert weight_gigabytes(70, "8-bit") == 70.0
print("memory_estimate: all checks passed")
