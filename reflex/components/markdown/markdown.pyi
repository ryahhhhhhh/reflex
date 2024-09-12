"""Stub file for reflex/components/markdown/markdown.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from functools import lru_cache
from typing import Any, Callable, Dict, Optional, Union, overload

from reflex.components.component import Component
from reflex.event import EventHandler, EventSpec
from reflex.ivars.base import LiteralVar, Var
from reflex.style import Style
from reflex.utils.imports import ImportDict

_CHILDREN = Var.create_safe("children")
_PROPS = Var.create_safe("...props")
_PROPS_IN_TAG = Var.create_safe("{...props}")
_MOCK_ARG = Var.create_safe("")
_REMARK_MATH = Var.create_safe("remarkMath")
_REMARK_GFM = Var.create_safe("remarkGfm")
_REMARK_UNWRAP_IMAGES = Var.create_safe("remarkUnwrapImages")
_REMARK_PLUGINS = LiteralVar.create([_REMARK_MATH, _REMARK_GFM, _REMARK_UNWRAP_IMAGES])
_REHYPE_KATEX = Var.create_safe("rehypeKatex")
_REHYPE_RAW = Var.create_safe("rehypeRaw")
_REHYPE_PLUGINS = LiteralVar.create([_REHYPE_KATEX, _REHYPE_RAW])
NO_PROPS_TAGS = ("ul", "ol", "li")

@lru_cache
def get_base_component_map() -> dict[str, Callable]: ...

class Markdown(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        component_map: Optional[Dict[str, Any]] = None,
        component_map_hash: Optional[str] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_click: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_focus: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_mount: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "Markdown":
        """Create a markdown component.

        Args:
            *children: The children of the component.
            component_map: The component map from a tag to a lambda that creates a component.
            component_map_hash: The hash of the component map, generated at create() time.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The markdown component.
        """
        ...

    def add_imports(self) -> ImportDict | list[ImportDict]: ...
    def get_component(self, tag: str, **props) -> Component: ...
    def format_component(self, tag: str, **props) -> str: ...
    def format_component_map(self) -> dict[str, Var]: ...
