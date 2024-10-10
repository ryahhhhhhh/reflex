"""Stub file for reflex/components/radix/themes/components/radio_cards.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from types import SimpleNamespace
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

from ..base import RadixThemesComponent

class RadioCardsRoot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        size: Optional[
            Union[
                Breakpoints[str, Literal["1", "2", "3"]],
                Literal["1", "2", "3"],
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
            ]
        ] = None,
        variant: Optional[
            Union[Literal["classic", "surface"], Var[Literal["classic", "surface"]]]
        ] = None,
        color_scheme: Optional[
            Union[
                Literal[
                    "amber",
                    "blue",
                    "bronze",
                    "brown",
                    "crimson",
                    "cyan",
                    "gold",
                    "grass",
                    "gray",
                    "green",
                    "indigo",
                    "iris",
                    "jade",
                    "lime",
                    "mint",
                    "orange",
                    "pink",
                    "plum",
                    "purple",
                    "red",
                    "ruby",
                    "sky",
                    "teal",
                    "tomato",
                    "violet",
                    "yellow",
                ],
                Var[
                    Literal[
                        "amber",
                        "blue",
                        "bronze",
                        "brown",
                        "crimson",
                        "cyan",
                        "gold",
                        "grass",
                        "gray",
                        "green",
                        "indigo",
                        "iris",
                        "jade",
                        "lime",
                        "mint",
                        "orange",
                        "pink",
                        "plum",
                        "purple",
                        "red",
                        "ruby",
                        "sky",
                        "teal",
                        "tomato",
                        "violet",
                        "yellow",
                    ]
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[Var[bool], bool]] = None,
        columns: Optional[
            Union[
                Breakpoints[
                    str,
                    Union[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"], str],
                ],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Union[
                                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                                str,
                            ],
                        ],
                        Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        str,
                    ]
                ],
                str,
            ]
        ] = None,
        gap: Optional[
            Union[
                Breakpoints[
                    str,
                    Union[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"], str],
                ],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Union[
                                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                                str,
                            ],
                        ],
                        Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        str,
                    ]
                ],
                str,
            ]
        ] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        value: Optional[Union[Var[str], str]] = None,
        name: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
        orientation: Optional[
            Union[
                Literal["horizontal", "undefined", "vertical"],
                Var[Literal["horizontal", "undefined", "vertical"]],
            ]
        ] = None,
        dir: Optional[Union[Literal["ltr", "rtl"], Var[Literal["ltr", "rtl"]]]] = None,
        loop: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        on_value_change: Optional[EventType] = None,
        **props,
    ) -> "RadioCardsRoot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: The size of the checkbox cards: "1" | "2" | "3"
            variant: Variant of button: "classic" | "surface" | "soft"
            color_scheme: Override theme color for button
            high_contrast: Uses a higher contrast color for the component.
            columns: The number of columns:
            gap: The gap between the checkbox cards:
            value: The controlled value of the radio item to check. Should be used in conjunction with onValueChange.
            name: The name of the group. Submitted with its owning form as part of a name/value pair.
            disabled: When true, prevents the user from interacting with radio items.
            required: When true, indicates that the user must check a radio item before the owning form can be submitted.
            orientation: The orientation of the component.
            dir: The reading direction of the radio group. If omitted,  inherits globally from DirectionProvider or assumes LTR (left-to-right) reading mode.
            loop: When true, keyboard navigation will loop from last item to first, and vice versa.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class RadioCardsItem(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        value: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "RadioCardsItem":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            value: The value given as data when submitted with a name.
            disabled: When true, prevents the user from interacting with the radio item.
            required: When true, indicates that the user must check the radio item before the owning form can be submitted.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class RadioCards(SimpleNamespace):
    root = staticmethod(RadioCardsRoot.create)
    item = staticmethod(RadioCardsItem.create)

radio_cards = RadioCards()
