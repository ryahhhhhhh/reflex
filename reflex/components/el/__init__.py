"""The el package exports raw HTML elements."""

# from .elements import *


MODULES = ("div", "Div")

def __getattr__(name: str):
    import importlib
    try:
        mod = importlib.import_module(".elements", package="reflex.components.el")
        return getattr(mod, name)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"The module {name} was not found in el")
    # if (mod := (name.split("reflex.components.radix.themes.")[-1].split(".")[0]) )in MODULES:
    #     module = importlib.import_module(f".{mod}", package="reflex.components.radix.themes")
    #     return getattr(module, name.split(".")[-1])
    # raise ModuleNotFoundError(f"The module {name} could not be found")