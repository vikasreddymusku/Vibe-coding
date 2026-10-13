"""Choosing a data structure: remove duplicate emails but keep the first-seen order."""


def unique_in_order(items):
    seen = set()          # a set answers "have I seen this?" quickly
    result = []           # a list keeps the order
    for item in items:
        key = item.strip().lower()
        if key not in seen:
            seen.add(key)
            result.append(key)
    return result


if __name__ == "__main__":
    raw = ["Ann@x.com", "bob@x.com", " ann@x.com", "BOB@x.com", "cy@x.com"]
    print(unique_in_order(raw))
