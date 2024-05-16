"""Core Reflex components."""

# from . import layout as layout
# from .banner import ConnectionBanner, ConnectionModal, ConnectionPulser
# from .colors import color
# from .cond import Cond, color_mode_cond, cond
# from .debounce import DebounceInput
# from .foreach import Foreach
# from .html import Html
# from .match import Match
# from reflex.utils import console
# from .responsive import (
#     desktop_only,
#     mobile_and_tablet,
#     mobile_only,
#     tablet_and_desktop,
#     tablet_only,
# )
# from .upload import (
#     UploadNamespace,
#     cancel_upload,
#     clear_selected_files,
#     get_upload_dir,
#     get_upload_url,
#     selected_files,
# )
from reflex.utils import console
#
_MAPPING = {
    "banner": ["connection_banner", "ConnectionBanner", "connection_modal", "ConnectionModal", "connection_pulser", "ConnectionPulser"],
    "debounce": ["debounce_input", "DebounceInput"],
    "foreach": ["Foreach", "foreach"],
    "html": ["html", "Html"],
    "match": ["match", "Match"],
    "upload": ["upload", "cancel_upload", "clear_selected_files", "get_upload_dir", "get_upload_url", "selected_files"]
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
#
#
# # _MAPPING = {value: key for key, values in _MAPPING.items() for value in values}
_MAPPING = _reverse_mapping(_MAPPING)
def __getattr__(name):
    # print(f"name: {name}")
    import importlib

    try:
        # mod = name.split("reflex.components.core.")[-1].split(".")[0]
        module = importlib.import_module(f".{_MAPPING[name]}", "reflex.components.core")
        return getattr(module, name.split(".")[-1])
    except ModuleNotFoundError:
        raise AttributeError(f"module 'reflex' has no attribute {name}") from None


# connection_banner = ConnectionBanner.create
# connection_modal = ConnectionModal.create
# connection_pulser = ConnectionPulser.create
# debounce_input = DebounceInput.create
# foreach = Foreach.create
# html = Html.create
# match = Match.create
# upload = UploadNamespace()
