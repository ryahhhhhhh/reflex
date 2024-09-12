"""Stub file for reflex/components/radix/themes/layout/container.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import elements
from reflex.event import EventHandler, EventSpec
from reflex.ivars.base import Var
from reflex.style import Style

from ..base import RadixThemesComponent

LiteralContainerSize = Literal["1", "2", "3", "4"]

class Container(elements.Div, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        padding: Optional[str] = "16px",
        stack_children_full_width: Optional[bool] = False,
        size: Optional[
            Union[
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3", "4"]],
                        Literal["1", "2", "3", "4"],
                    ]
                ],
                Literal["1", "2", "3", "4"],
                Breakpoints[str, Literal["1", "2", "3", "4"]],
            ]
        ] = None,
        access_key: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        draggable: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        input_mode: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        item_prop: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        spell_check: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        tab_index: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        title: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
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
    ) -> "Container":
        """Create the container component.

        Args:
            children: The children components.
            padding: The padding of the container.
            stack_children_full_width: If True, any vstack/hstack children will have 100% width.
            props: The properties of the container.

        Returns:
            The container component.
        """
        ...

container = Container.create
