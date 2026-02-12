from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.vendors.cisco import CiscoPack


def test_cisco_pack_matches_vendor():
    p = CiscoPack()
    ident = DeviceIdentity(
        device_id="c1",
        vendor="cisco",
        os_name="iosxr",
        model="8000",
        mgmt_address="10.0.0.10",
    )
    assert p.match(ident) is True


def test_cisco_pack_returns_system_group_when_openconfig_supported():
    p = CiscoPack()
    groups = p.sensor_groups(supports_openconfig=True)

    assert len(groups) == 1
    assert groups[0].name == "system"
    assert groups[0].sample_interval_s == 10.0
    assert len(groups[0].paths) == 1
    assert groups[0].paths[0].origin == "openconfig"
