from reflex.components.core.banner import (
    ConnectionBanner,
    ConnectionModal,
    ConnectionPulser,
    WebsocketTargetURL,
)
from reflex.components.radix.themes.typography.text import Text


def test_websocket_target_url():
    url = WebsocketTargetURL.create()
    _imports = url._get_all_imports()
    assert [i.library for i in _imports] == ["/utils/state", "/env.json"]


def test_connection_banner():
    banner = ConnectionBanner.create()
    _imports = banner._get_all_imports()
    assert [i.library for i in _imports] == [
        "react",
        "/utils/context",
        "/utils/state",
        "@radix-ui/themes",
        "/env.json",
    ]

    msg = "Connection error"
    custom_banner = ConnectionBanner.create(Text.create(msg))
    assert msg in str(custom_banner.render())


def test_connection_modal():
    modal = ConnectionModal.create()
    _imports = modal._get_all_imports()
    assert [i.library for i in _imports] == [
        "react",
        "/utils/context",
        "/utils/state",
        "@radix-ui/themes",
        "/env.json",
    ]

    msg = "Connection error"
    custom_modal = ConnectionModal.create(Text.create(msg))
    assert msg in str(custom_modal.render())


def test_connection_pulser():
    pulser = ConnectionPulser.create()
    _custom_code = pulser._get_all_custom_code()
    _imports = pulser._get_all_imports()
