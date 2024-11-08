"""Stub file for reflex/components/recharts/polar.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, List, Literal, Optional, Union, overload

from reflex.constants.colors import Color
from reflex.event import BASE_STATE, EventType
from reflex.style import Style
from reflex.vars.base import Var

from .recharts import Recharts

class Pie(Recharts):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        data: Optional[Union[List[Dict[str, Any]], Var[List[Dict[str, Any]]]]] = None,
        data_key: Optional[Union[Var[Union[int, str]], int, str]] = None,
        cx: Optional[Union[Var[Union[int, str]], int, str]] = None,
        cy: Optional[Union[Var[Union[int, str]], int, str]] = None,
        inner_radius: Optional[Union[Var[Union[int, str]], int, str]] = None,
        outer_radius: Optional[Union[Var[Union[int, str]], int, str]] = None,
        start_angle: Optional[Union[Var[int], int]] = None,
        end_angle: Optional[Union[Var[int], int]] = None,
        min_angle: Optional[Union[Var[int], int]] = None,
        padding_angle: Optional[Union[Var[int], int]] = None,
        name_key: Optional[Union[Var[str], str]] = None,
        legend_type: Optional[
            Union[
                Literal[
                    "circle",
                    "cross",
                    "diamond",
                    "line",
                    "none",
                    "plainline",
                    "rect",
                    "square",
                    "star",
                    "triangle",
                    "wye",
                ],
                Var[
                    Literal[
                        "circle",
                        "cross",
                        "diamond",
                        "line",
                        "none",
                        "plainline",
                        "rect",
                        "square",
                        "star",
                        "triangle",
                        "wye",
                    ]
                ],
            ]
        ] = None,
        label: Optional[Union[Var[bool], bool]] = None,
        label_line: Optional[Union[Var[bool], bool]] = None,
        stroke: Optional[Union[Color, Var[Union[Color, str]], str]] = None,
        fill: Optional[Union[Color, Var[Union[Color, str]], str]] = None,
        is_animation_active: Optional[Union[Var[bool], bool]] = None,
        animation_begin: Optional[Union[Var[int], int]] = None,
        animation_duration: Optional[Union[Var[int], int]] = None,
        animation_easing: Optional[
            Union[
                Literal["ease", "ease-in", "ease-in-out", "ease-out", "linear"],
                Var[Literal["ease", "ease-in", "ease-in-out", "ease-out", "linear"]],
            ]
        ] = None,
        root_tab_index: Optional[Union[Var[int], int]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_animation_end: Optional[EventType[[], BASE_STATE]] = None,
        on_animation_start: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_enter: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_leave: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_move: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_out: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_over: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "Pie":
        """Create the component.

        Args:
            *children: The children of the component.
            data: The index of active sector in Pie, this option can be changed in mouse event handlers.
            data_key: The key of each sector's value.
            cx: The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width. Default: "50%"
            cy: The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height. Default: "50%"
            inner_radius: The inner radius of pie, which can be set to a percent value. Default: 0
            outer_radius: The outer radius of pie, which can be set to a percent value. Default: "80%"
            start_angle: The angle of first sector. Default: 0
            end_angle: The end angle of last sector, which should be unequal to start_angle. Default: 360
            min_angle: The minimum angle of each unzero data. Default: 0
            padding_angle: The angle between two sectors. Default: 0
            name_key: The key of each sector's name. Default: "name"
            legend_type: The type of icon in legend. If set to 'none', no legend item will be rendered. Default: "rect"
            label: If false set, labels will not be drawn. If true set, labels will be drawn which have the props calculated internally. Default: False
            label_line: If false set, label lines will not be drawn. If true set, label lines will be drawn which have the props calculated internally. Default: False
            stroke: Stoke color. Default: rx.color("accent", 9)
            fill: Fill color. Default: rx.color("accent", 3)
            is_animation_active: If set false, animation of tooltip will be disabled. Default: true in CSR, and false in SSR
            animation_begin: Specifies when the animation should begin, the unit of this option is ms. Default: 400
            animation_duration: Specifies the duration of animation, the unit of this option is ms. Default: 1500
            animation_easing: The type of easing function. Default: "ease"
            root_tab_index: The tabindex of wrapper surrounding the cells. Default: 0
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

class Radar(Recharts):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        data_key: Optional[Union[Var[Union[int, str]], int, str]] = None,
        points: Optional[Union[List[Dict[str, Any]], Var[List[Dict[str, Any]]]]] = None,
        dot: Optional[Union[Var[bool], bool]] = None,
        stroke: Optional[Union[Color, Var[Union[Color, str]], str]] = None,
        fill: Optional[Union[Var[str], str]] = None,
        fill_opacity: Optional[Union[Var[float], float]] = None,
        legend_type: Optional[
            Union[
                Literal[
                    "circle",
                    "cross",
                    "diamond",
                    "line",
                    "none",
                    "plainline",
                    "rect",
                    "square",
                    "star",
                    "triangle",
                    "wye",
                ],
                Var[
                    Literal[
                        "circle",
                        "cross",
                        "diamond",
                        "line",
                        "none",
                        "plainline",
                        "rect",
                        "square",
                        "star",
                        "triangle",
                        "wye",
                    ]
                ],
            ]
        ] = None,
        label: Optional[Union[Var[bool], bool]] = None,
        is_animation_active: Optional[Union[Var[bool], bool]] = None,
        animation_begin: Optional[Union[Var[int], int]] = None,
        animation_duration: Optional[Union[Var[int], int]] = None,
        animation_easing: Optional[
            Union[
                Literal["ease", "ease-in", "ease-in-out", "ease-out", "linear"],
                Var[Literal["ease", "ease-in", "ease-in-out", "ease-out", "linear"]],
            ]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_animation_end: Optional[EventType[[], BASE_STATE]] = None,
        on_animation_start: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "Radar":
        """Create the component.

        Args:
            *children: The children of the component.
            data_key: The key of a group of data which should be unique in a radar chart.
            points: The coordinates of all the vertexes of the radar shape, like [{ x, y }].
            dot: If false set, dots will not be drawn. Default: True
            stroke: Stoke color. Default: rx.color("accent", 9)
            fill: Fill color. Default: rx.color("accent", 3)
            fill_opacity: opacity. Default: 0.6
            legend_type: The type of icon in legend. If set to 'none', no legend item will be rendered. Default: "rect"
            label: If false set, labels will not be drawn. Default: True
            is_animation_active: If set false, animation of polygon will be disabled. Default: True in CSR, and False in SSR
            animation_begin: Specifies when the animation should begin, the unit of this option is ms. Default: 0
            animation_duration: Specifies the duration of animation, the unit of this option is ms. Default: 1500
            animation_easing: The type of easing function. 'ease' | 'ease-in' | 'ease-out' | 'ease-in-out' | 'linear'. Default: "ease"
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

class RadialBar(Recharts):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        data: Optional[Union[List[Dict[str, Any]], Var[List[Dict[str, Any]]]]] = None,
        data_key: Optional[Union[Var[Union[int, str]], int, str]] = None,
        min_angle: Optional[Union[Var[int], int]] = None,
        legend_type: Optional[
            Union[
                Literal[
                    "circle",
                    "cross",
                    "diamond",
                    "line",
                    "none",
                    "plainline",
                    "rect",
                    "square",
                    "star",
                    "triangle",
                    "wye",
                ],
                Var[
                    Literal[
                        "circle",
                        "cross",
                        "diamond",
                        "line",
                        "none",
                        "plainline",
                        "rect",
                        "square",
                        "star",
                        "triangle",
                        "wye",
                    ]
                ],
            ]
        ] = None,
        label: Optional[
            Union[Dict[str, Any], Var[Union[Dict[str, Any], bool]], bool]
        ] = None,
        background: Optional[
            Union[Dict[str, Any], Var[Union[Dict[str, Any], bool]], bool]
        ] = None,
        is_animation_active: Optional[Union[Var[bool], bool]] = None,
        animation_begin: Optional[Union[Var[int], int]] = None,
        animation_duration: Optional[Union[Var[int], int]] = None,
        animation_easing: Optional[
            Union[
                Literal["ease", "ease-in", "ease-in-out", "ease-out", "linear"],
                Var[Literal["ease", "ease-in", "ease-in-out", "ease-out", "linear"]],
            ]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_animation_end: Optional[EventType[[], BASE_STATE]] = None,
        on_animation_start: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_enter: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_leave: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_move: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_out: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_over: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "RadialBar":
        """Create the component.

        Args:
            *children: The children of the component.
            data: The source data which each element is an object.
            data_key: The key of a group of data which should be unique to show the meaning of angle axis.
            min_angle: Min angle of each bar. A positive value between 0 and 360. Default: 0
            legend_type: The type of icon in legend. If set to 'none', no legend item will be rendered. Default: "rect"
            label: If false set, labels will not be drawn. If true set, labels will be drawn which have the props calculated internally. Default: False
            background: If false set, background sector will not be drawn. Default: False
            is_animation_active: If set false, animation of radial bars will be disabled. Default: True
            animation_begin: Specifies when the animation should begin, the unit of this option is ms. Default: 0
            animation_duration: Specifies the duration of animation, the unit of this option is ms. Default 1500
            animation_easing: The type of easing function. 'ease' | 'ease-in' | 'ease-out' | 'ease-in-out' | 'linear'. Default: "ease"
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

class PolarAngleAxis(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        data_key: Optional[Union[Var[Union[int, str]], int, str]] = None,
        cx: Optional[Union[Var[Union[int, str]], int, str]] = None,
        cy: Optional[Union[Var[Union[int, str]], int, str]] = None,
        radius: Optional[Union[Var[Union[int, str]], int, str]] = None,
        axis_line: Optional[
            Union[Dict[str, Any], Var[Union[Dict[str, Any], bool]], bool]
        ] = None,
        axis_line_type: Optional[
            Union[Literal["circle", "polygon"], Var[Literal["circle", "polygon"]]]
        ] = None,
        tick_line: Optional[
            Union[Dict[str, Any], Var[Union[Dict[str, Any], bool]], bool]
        ] = None,
        tick: Optional[
            Union[Dict[str, Any], Var[Union[Dict[str, Any], bool]], bool]
        ] = None,
        ticks: Optional[Union[List[Dict[str, Any]], Var[List[Dict[str, Any]]]]] = None,
        orientation: Optional[Union[Var[str], str]] = None,
        stroke: Optional[Union[Color, Var[Union[Color, str]], str]] = None,
        allow_duplicated_category: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
        on_mount: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_down: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_enter: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_leave: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_move: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_out: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_over: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_up: Optional[EventType[[], BASE_STATE]] = None,
        on_scroll: Optional[EventType[[], BASE_STATE]] = None,
        on_unmount: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "PolarAngleAxis":
        """Create the component.

        Args:
            *children: The children of the component.
            data_key: The key of a group of data which should be unique to show the meaning of angle axis.
            cx: The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width.
            cy: The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height.
            radius: The outer radius of circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.
            axis_line: If false set, axis line will not be drawn. If true set, axis line will be drawn which have the props calculated internally. If object set, axis line will be drawn which have the props mergered by the internal calculated props and the option. Default: True
            axis_line_type: The type of axis line. Default: "polygon"
            tick_line: If false set, tick lines will not be drawn. If true set, tick lines will be drawn which have the props calculated internally. If object set, tick lines will be drawn which have the props mergered by the internal calculated props and the option. Default: False
            tick: If false set, ticks will not be drawn. If true set, ticks will be drawn which have the props calculated internally. If object set, ticks will be drawn which have the props mergered by the internal calculated props and the option. Default: True
            ticks: The array of every tick's value and angle.
            orientation: The orientation of axis text. Default: "outer"
            stroke: The stroke color of axis. Default: rx.color("gray", 10)
            allow_duplicated_category: Allow the axis has duplicated categorys or not when the type of axis is "category". Default: True
            on_click: The customized event handler of click on the ticks of this axis.
            on_mouse_down: The customized event handler of mousedown on the the ticks of this axis.
            on_mouse_up: The customized event handler of mouseup on the ticks of this axis.
            on_mouse_move: The customized event handler of mousemove on the ticks of this axis.
            on_mouse_over: The customized event handler of mouseover on the ticks of this axis.
            on_mouse_out: The customized event handler of mouseout on the ticks of this axis.
            on_mouse_enter: The customized event handler of moustenter on the ticks of this axis.
            on_mouse_leave: The customized event handler of mouseleave on the ticks of this axis.
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

class PolarGrid(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        cx: Optional[Union[Var[int], int]] = None,
        cy: Optional[Union[Var[int], int]] = None,
        inner_radius: Optional[Union[Var[int], int]] = None,
        outer_radius: Optional[Union[Var[int], int]] = None,
        polar_angles: Optional[Union[List[int], Var[List[int]]]] = None,
        polar_radius: Optional[Union[List[int], Var[List[int]]]] = None,
        grid_type: Optional[
            Union[Literal["circle", "polygon"], Var[Literal["circle", "polygon"]]]
        ] = None,
        stroke: Optional[Union[Color, Var[Union[Color, str]], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[[], BASE_STATE]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_context_menu: Optional[EventType[[], BASE_STATE]] = None,
        on_double_click: Optional[EventType[[], BASE_STATE]] = None,
        on_focus: Optional[EventType[[], BASE_STATE]] = None,
        on_mount: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_down: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_enter: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_leave: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_move: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_out: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_over: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_up: Optional[EventType[[], BASE_STATE]] = None,
        on_scroll: Optional[EventType[[], BASE_STATE]] = None,
        on_unmount: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "PolarGrid":
        """Create the component.

        Args:
            *children: The children of the component.
            cx: The x-coordinate of center.
            cy: The y-coordinate of center.
            inner_radius: The radius of the inner polar grid.
            outer_radius: The radius of the outer polar grid.
            polar_angles: The array of every line grid's angle.
            polar_radius: The array of every line grid's radius.
            grid_type: The type of polar grids. 'polygon' | 'circle'. Default: "polygon"
            stroke: The stroke color of grid. Default: rx.color("gray", 10)
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

class PolarRadiusAxis(Recharts):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        angle: Optional[Union[Var[int], int]] = None,
        type_: Optional[
            Union[Literal["category", "number"], Var[Literal["category", "number"]]]
        ] = None,
        allow_duplicated_category: Optional[Union[Var[bool], bool]] = None,
        cx: Optional[Union[Var[int], int]] = None,
        cy: Optional[Union[Var[int], int]] = None,
        reversed: Optional[Union[Var[bool], bool]] = None,
        orientation: Optional[
            Union[
                Literal["left", "middle", "right"],
                Var[Literal["left", "middle", "right"]],
            ]
        ] = None,
        axis_line: Optional[
            Union[Dict[str, Any], Var[Union[Dict[str, Any], bool]], bool]
        ] = None,
        tick: Optional[
            Union[Dict[str, Any], Var[Union[Dict[str, Any], bool]], bool]
        ] = None,
        tick_count: Optional[Union[Var[int], int]] = None,
        scale: Optional[
            Union[
                Literal[
                    "auto",
                    "band",
                    "identity",
                    "linear",
                    "log",
                    "ordinal",
                    "point",
                    "pow",
                    "quantile",
                    "quantize",
                    "sequential",
                    "sqrt",
                    "threshold",
                    "time",
                    "utc",
                ],
                Var[
                    Literal[
                        "auto",
                        "band",
                        "identity",
                        "linear",
                        "log",
                        "ordinal",
                        "point",
                        "pow",
                        "quantile",
                        "quantize",
                        "sequential",
                        "sqrt",
                        "threshold",
                        "time",
                        "utc",
                    ]
                ],
            ]
        ] = None,
        domain: Optional[
            Union[List[Union[int, str]], Var[List[Union[int, str]]]]
        ] = None,
        stroke: Optional[Union[Color, Var[Union[Color, str]], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_click: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_enter: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_leave: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_move: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_out: Optional[EventType[[], BASE_STATE]] = None,
        on_mouse_over: Optional[EventType[[], BASE_STATE]] = None,
        **props,
    ) -> "PolarRadiusAxis":
        """Create the component.

        Args:
            *children: The children of the component.
            angle: The angle of radial direction line to display axis text. Default: 0
            type_: The type of axis line. 'number' | 'category'. Default: "category"
            allow_duplicated_category: Allow the axis has duplicated categorys or not when the type of axis is "category". Default: True
            cx: The x-coordinate of center.
            cy: The y-coordinate of center.
            reversed: If set to true, the ticks of this axis are reversed. Default: False
            orientation: The orientation of axis text. Default: "right"
            axis_line: If false set, axis line will not be drawn. If true set, axis line will be drawn which have the props calculated internally. If object set, axis line will be drawn which have the props mergered by the internal calculated props and the option. Default: True
            tick: If false set, ticks will not be drawn. If true set, ticks will be drawn which have the props calculated internally. If object set, ticks will be drawn which have the props mergered by the internal calculated props and the option. Default: True
            tick_count: The count of axis ticks. Not used if 'type' is 'category'. Default: 5
            scale: If 'auto' set, the scale funtion is linear scale. 'auto' | 'linear' | 'pow' | 'sqrt' | 'log' | 'identity' | 'time' | 'band' | 'point' | 'ordinal' | 'quantile' | 'quantize' | 'utc' | 'sequential' | 'threshold'. Default: "auto"
            domain: The domain of the polar radius axis, specifying the minimum and maximum values. Default: [0, "auto"]
            stroke: The stroke color of axis. Default: rx.color("gray", 10)
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

pie = Pie.create
radar = Radar.create
radial_bar = RadialBar.create
polar_angle_axis = PolarAngleAxis.create
polar_grid = PolarGrid.create
polar_radius_axis = PolarRadiusAxis.create
