"""Stub file for reflex/components/radix/primitives/progress.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.component import ComponentNamespace
from reflex.components.radix.primitives.base import RadixPrimitiveComponentWithClassName
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

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
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
        as_child: Optional[Union[Var[bool], bool]] = None,
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
        value: Optional[Union[Var[Optional[int]], int]] = None,
        max: Optional[Union[Var[Optional[int]], int]] = None,
        radius: Optional[
            Union[
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
        value: Optional[Union[Var[Optional[int]], int]] = None,
        max: Optional[Union[Var[Optional[int]], int]] = None,
        radius: Optional[
            Union[
                Literal["full", "large", "medium", "none", "small"],
                Var[Literal["full", "large", "medium", "none", "small"]],
            ]
        ] = None,
        as_child: Optional[Union[Var[bool], bool]] = None,
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
