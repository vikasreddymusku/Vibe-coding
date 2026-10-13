"""Programming concepts in one small script: variables, a function, a loop, a condition."""

PASS_MARK = 50  # a constant: a value that should not change


def letter_grade(score):
    """Return a letter for a score from 0 to 100."""
    if score >= 80:
        return "A"
    elif score >= PASS_MARK:
        return "B"
    return "F"


def report(students):
    """Build one line per student and count how many passed."""
    lines = []
    passed = 0
    for name, score in students.items():  # a loop over key/value pairs
        grade = letter_grade(score)
        if grade != "F":
            passed += 1
        lines.append(f"{name}: {score} -> {grade}")
    lines.append(f"Passed: {passed} of {len(students)}")
    return lines


if __name__ == "__main__":
    data = {"Asha": 91, "Ben": 64, "Chen": 38}
    print("\n".join(report(data)))
