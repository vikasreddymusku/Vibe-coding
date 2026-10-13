from unique_emails import unique_in_order

assert unique_in_order(["Ann@x.com", "bob@x.com", " ann@x.com", "BOB@x.com", "cy@x.com"]) == ["ann@x.com", "bob@x.com", "cy@x.com"]
assert unique_in_order([]) == []
assert unique_in_order(["a@x.com"] * 3) == ["a@x.com"]
print("unique_emails: all checks passed")
