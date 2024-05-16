"""Import all the components."""
from __future__ import annotations

# from . import lucide
# from .base import Fragment, Script, fragment, script
from .component import Component
from reflex.utils import console
# from .component import NoSSRComponent as NoSSRComponent
# from .core import *
# from .datadisplay import *
# from .el import img as image
# from .gridjs import *
# from .markdown import *
# from .moment import *
# from .next import NextLink, next_link
# from .plotly import *
# from .radix import *
# from .react_player import *
# from .sonner import *
# from .suneditor import *
#
# icon = lucide.icon

from . import radix, el, core

_MAPPING = {
    "reflex.components.component": ["Component", "NoSSRComponent", "memo"],
    "reflex.components.chakra": ["chakra"],
    "reflex.components.el": ["el"],
    "reflex.components.lucide": ["lucide"],
    "reflex.components.next": ["next"],
    "reflex.components.radix": ["radix", "color_mode"],
    "reflex.components.radix.themes.layout": ["center"],
    "reflex.components.core": ["color",
                               "cond",
                               "foreach",
                               "html",
                               "match",
                               "color_mode_cond",
                               "connection_banner",
                               "connection_modal",
                               "debounce_input", ],
    "reflex.components.recharts": ["recharts"],
    "reflex.components.moment.moment": ["MomentDelta"],

}

def _reverse_mapping(mapping: dict[str, list]) -> dict[str, str]:
    """Reverse the mapping used to lazy loading, and check for conflicting name.

    Args:
        mapping: The mapping to reverse.

    Returns:
        The reversed mapping.
    """
    reversed_mapping = {}
    for key, values in mapping.items():
        for value in values:
            if value not in reversed_mapping:
                reversed_mapping[value] = key
            else:
                console.warn(
                    f"Key {value} is present multiple times in the imports _MAPPING: {key} / {reversed_mapping[value]}"
                )
    return reversed_mapping


# _MAPPING = {value: key for key, values in _MAPPING.items() for value in values}
_MAPPING = _reverse_mapping(_MAPPING)
def __getattr__(name):
    import importlib
    import sys

    try:
        mod = importlib.import_module(_MAPPING[name])
        return (
            getattr(mod, name) if name != _MAPPING[name].rsplit(".")[-1] else mod
        )
    except ModuleNotFoundError:
        raise AttributeError(f"module 'reflex' has no attribute {name}") from None
    # modules = importlib.import_module("reflex.components.radix")
    # v = getattr(modules, name)
    # return v