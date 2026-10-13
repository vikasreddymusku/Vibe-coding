"""Check that a function or class an AI suggested really exists, before you rely on it."""
import importlib


def symbol_exists(module_name, attribute):
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        return False
    return hasattr(module, attribute)


if __name__ == "__main__":
    for module, name in [("json", "loads"), ("json", "parse"), ("math", "cbrt"), ("no_such_module", "x")]:
        print(f"{module}.{name}: {symbol_exists(module, name)}")
