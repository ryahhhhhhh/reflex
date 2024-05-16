"""Namespace for components provided by the @radix-ui/themes library."""
# from .base import theme as theme
# from .base import theme_panel as theme_panel
# from .color_mode import color_mode_var_and_namespace as color_mode
# from .components import *
# from .layout import *
# from .typography import *

MODULES = ("base", "color_mode", "layout", "typography")
# # from reflex import Import
from reflex.utils import console
_MAPPING = {
    "base": ["theme", "theme_panel"],
    "color_mode": ["color_mode_var_and_namespace"],
    "components": [
        "alert_dialog",
        "aspect_ratio",
        "avatar",
        "badge",
        "button",
        "callout",
        "card",
        "checkbox",
        "checkbox_cards",
        "checkbox_group",
        "context_menu",
        "data_list",
        "dialog",
        "divider",
        "dropdown_menu",
        "hover_card",
        "icon_button",
        "input",
        "inset",
        "menu",
        "popover",
        "radio",
        "radio_cards",
        "radio_group",
        "scroll_area",
        "segmented_control",
        "select",
        "separator",
        "skeleton",
        "slider",
        "spinner",
        "switch",
        "table",
        "tabs",
        "text_area",
        "text_field",
        "tooltip",
    ]
    ,
    "layouts": [
        "box",
        "center",
        "container",
        "flex",
        "grid",
        "section",
        "spacer",
        "stack",
        "hstack",
        "vstack",
        "list",
        "list_item",
        "ordered_list",
        "unordered_list",
    ],
    "typography": [
        "blockquote",
        "code",
        "heading",
        "link",
        "text",
    ]

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

_MAPPING = _reverse_mapping(_MAPPING)

def __getattr__(name: str):
    try:
        import importlib
        # if (mod := (name.split("reflex.components.radix.themes.")[-1].split(".")[0]) )in MODULES:
        module = importlib.import_module(f".{_MAPPING[name]}", package="reflex.components.radix.themes")
        return getattr(module, name.split(".")[-1])
    except ModuleNotFoundError:
        raise AttributeError(f"module 'reflex' has no attribute {name}")
