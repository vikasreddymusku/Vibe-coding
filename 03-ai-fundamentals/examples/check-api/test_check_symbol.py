from check_symbol import symbol_exists
assert symbol_exists("json", "loads") is True          # real
assert symbol_exists("json", "parse") is False         # JavaScript's JSON.parse, not Python
assert symbol_exists("no_such_module", "anything") is False
assert symbol_exists("os.path", "join") is True
print("check_symbol: all checks passed")
