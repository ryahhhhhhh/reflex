"""Stub file for reflex/components/radix/primitives/progress.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Literal, Optional, Union, overload

from reflex.components.component import ComponentNamespace
from reflex.components.radix.primitives.base import RadixPrimitiveComponentWithClassName
from reflex.event import EventHandler, EventSpec
from reflex.ivars.base import ImmutableVar
from reflex.style import Style
from reflex.vars import Var

class ProgressComponent(RadixPrimitiveComponentWithClassName):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[ImmutableVar, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "ProgressComponent":
        """Create the component.

        Args:
            *children: The children of the component.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class ProgressRoot(ProgressComponent):
    def add_style(self) -> dict[str, Any] | None: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        radius: Optional[
            Union[
                Var[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[ImmutableVar, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "ProgressRoot":
        """Create the component.

        Args:
            *children: The children of the component.
            radius: Override theme radius for progress bar: "none" | "small" | "medium" | "large" | "full"
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class ProgressIndicator(ProgressComponent):
    def add_style(self) -> dict[str, Any] | None: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        value: Optional[Union[Var[Optional[int]], int]] = None,
        max: Optional[Union[Var[Optional[int]], int]] = None,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[ImmutableVar, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "ProgressIndicator":
        """Create the component.

        Args:
            *children: The children of the component.
            value: The current progress value.
            max: The maximum progress value.
            color_scheme: The color scheme of the progress indicator.
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class Progress(ProgressRoot):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        value: Optional[Union[Var[Optional[int]], int]] = None,
        max: Optional[Union[Var[Optional[int]], int]] = None,
        radius: Optional[
            Union[
                Var[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[ImmutableVar, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "Progress":
        """High-level API for progress bar.

        Args:
            color_scheme: Override theme color for progress bar indicator
            value: The current progress value.
            max: The maximum progress value.
            radius: Override theme radius for progress bar: "none" | "small" | "medium" | "large" | "full"
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the progress bar.

        Returns:
            The progress bar.
        """
        ...

class ProgressNamespace(ComponentNamespace):
    root = staticmethod(ProgressRoot.create)
    indicator = staticmethod(ProgressIndicator.create)

    @staticmethod
    def __call__(
        *children,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        value: Optional[Union[Var[Optional[int]], int]] = None,
        max: Optional[Union[Var[Optional[int]], int]] = None,
        radius: Optional[
            Union[
                Var[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[ImmutableVar, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, ImmutableVar]
        ] = None,
        **props,
    ) -> "Progress":
        """High-level API for progress bar.

        Args:
            color_scheme: Override theme color for progress bar indicator
            value: The current progress value.
            max: The maximum progress value.
            radius: Override theme radius for progress bar: "none" | "small" | "medium" | "large" | "full"
            as_child: Change the default rendered element for the one passed as a child.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the progress bar.

        Returns:
            The progress bar.
        """
        ...

progress = ProgressNamespace()
