from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.vendors.nokia import NokiaPack


def test_nokia_pack_matches_vendor():
    p = NokiaPack()
    ident = DeviceIdentity(
        device_id="n1",
        vendor="nokia",
        os_name="sros",
        model="7750",
        mgmt_address="10.0.0.30",
    )
    assert p.match(ident) is True


def test_nokia_pack_returns_system_group_when_openconfig_supported():
    p = NokiaPack()
    groups = p.sensor_groups(supports_openconfig=True)

    assert len(groups) == 1
    assert groups[0].name == "system"
    assert groups[0].paths[0].origin == "openconfig"
