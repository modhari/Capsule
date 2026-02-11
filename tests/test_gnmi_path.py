from gnmi_collection_agent.gnmi.client import GnmiPath


def test_gnmi_path_is_value_object():
    p = GnmiPath(origin="openconfig", path="/system/state")
    assert p.origin == "openconfig"
    assert p.path.startswith("/")
