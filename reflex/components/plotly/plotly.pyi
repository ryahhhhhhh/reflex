"""Stub file for reflex/components/plotly/plotly.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Optional, Union, overload

from reflex.base import Base
from reflex.components.component import NoSSRComponent
from reflex.event import EventHandler, EventSpec
from reflex.ivars.base import Var
from reflex.style import Style
from reflex.utils import console

try:
    from plotly.graph_objects import Figure, layout

    Template = layout.Template
except ImportError:
    console.warn("Plotly is not installed. Please run `pip install plotly`.")
    Figure = Any
    Template = Any

class _ButtonClickData(Base):
    menu: Any
    button: Any
    active: Any

class Plotly(NoSSRComponent):
    def add_imports(self) -> dict[str, str]: ...
    def add_custom_code(self) -> list[str]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        data: Optional[Union[Var[Figure], Figure]] = None,  # type: ignore
        layout: Optional[Union[Var[Dict], Dict]] = None,
        template: Optional[Union[Var[Template], Template]] = None,  # type: ignore
        config: Optional[Union[Var[Dict], Dict]] = None,
        use_resize_handler: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_after_plot: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_animated: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_animating_frame: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_animation_interrupted: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_autosize: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_before_hover: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_blur: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_button_clicked: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_click: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_deselect: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_focus: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_hover: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
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
        on_redraw: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_relayout: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_relayouting: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_restyle: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_scroll: Optional[Union[EventHandler, EventSpec, list, Callable, Var]] = None,
        on_selected: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_selecting: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_transition_interrupted: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_transitioning: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_unhover: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, Var]
        ] = None,
        **props,
    ) -> "Plotly":
        """Create the Plotly component.

        Args:
            *children: The children of the component.
            data: The figure to display. This can be a plotly figure or a plotly data json.
            layout: The layout of the graph.
            template: The template for visual appearance of the graph.
            config: The config of the graph.
            use_resize_handler: If true, the graph will resize when the window is resized.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Plotly component.
        """
        ...
