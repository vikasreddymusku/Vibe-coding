from grade_report import letter_grade, report

assert letter_grade(80) == "A"
assert letter_grade(79) == "B"
assert letter_grade(50) == "B"
assert letter_grade(49) == "F"
assert report({"Asha": 91, "Ben": 64, "Chen": 38}) == [
    "Asha: 91 -> A", "Ben: 64 -> B", "Chen: 38 -> F", "Passed: 2 of 3"]
assert report({}) == ["Passed: 0 of 0"]
print("grade_report: all checks passed")
