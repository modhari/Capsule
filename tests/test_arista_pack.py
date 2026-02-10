from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.vendors.arista import AristaPack


def test_arista_pack_matches_vendor():
    p = AristaPack()
    ident = DeviceIdentity(
        device_id="d1",
        vendor="arista",
        os_name="eos",
        model="7050",
        mgmt_address="10.0.0.1",
    )
    assert p.match(ident) is True


def test_arista_pack_returns_system_group_when_openconfig_supported():
    p = AristaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    assert len(groups) == 1
    assert groups[0].name == "system"
    assert len(groups[0].paths) == 1
    assert groups[0].paths[0].origin == "openconfig"
