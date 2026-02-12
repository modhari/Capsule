from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.vendors.juniper import JuniperPack


def test_juniper_pack_matches_vendor():
    p = JuniperPack()
    ident = DeviceIdentity(
        device_id="j1",
        vendor="juniper",
        os_name="junos",
        model="mx",
        mgmt_address="10.0.0.20",
    )
    assert p.match(ident) is True


def test_juniper_pack_returns_system_group_when_openconfig_supported():
    p = JuniperPack()
    groups = p.sensor_groups(supports_openconfig=True)

    assert len(groups) == 1
    assert groups[0].name == "system"
    assert groups[0].paths[0].origin == "openconfig"
