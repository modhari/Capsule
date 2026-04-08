from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.vendors.nokia import NokiaPack


def test_nokia_pack_matches_vendor():
    p = NokiaPack()
    ident = DeviceIdentity(
        device_id="d1",
        vendor="nokia",
        os_name="srlinux",
        model="7220",
        mgmt_address="10.0.0.1",
    )
    assert p.match(ident) is True


def test_nokia_pack_does_not_match_other_vendor():
    p = NokiaPack()
    ident = DeviceIdentity(
        device_id="d2",
        vendor="arista",
        os_name="eos",
        model="7050",
        mgmt_address="10.0.0.2",
    )
    assert p.match(ident) is False


def test_nokia_pack_returns_srlinux_groups_without_openconfig():
    p = NokiaPack()
    groups = p.sensor_groups(supports_openconfig=False)
    names = [g.name for g in groups]
    assert "system" in names
    assert "bgp_session" in names
    assert "bgp_prefixes" in names


def test_nokia_pack_srlinux_bgp_session_uses_native_paths():
    p = NokiaPack()
    groups = p.sensor_groups(supports_openconfig=False)
    bgp = next(g for g in groups if g.name == "bgp_session")
    assert all(path.origin == "native" for path in bgp.paths)


def test_nokia_pack_srlinux_bgp_session_has_failure_reason_path():
    p = NokiaPack()
    groups = p.sensor_groups(supports_openconfig=False)
    bgp = next(g for g in groups if g.name == "bgp_session")
    path_strings = [p.path for p in bgp.paths]
    assert any("failure-reason" in p for p in path_strings)
    assert any("session-state" in p for p in path_strings)


def test_nokia_pack_returns_openconfig_groups_when_supported():
    p = NokiaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    names = [g.name for g in groups]
    assert "system" in names
    assert "bgp_session" in names
    assert "bgp_prefixes" in names
    assert "bgp_topology" in names


def test_nokia_pack_openconfig_bgp_session_uses_openconfig_origin():
    p = NokiaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    bgp = next(g for g in groups if g.name == "bgp_session")
    assert all(path.origin == "openconfig" for path in bgp.paths)


def test_nokia_pack_srlinux_prefixes_uses_native_paths():
    p = NokiaPack()
    groups = p.sensor_groups(supports_openconfig=False)
    prefixes = next(g for g in groups if g.name == "bgp_prefixes")
    path_strings = [p.path for p in prefixes.paths]
    assert any("received-routes" in p for p in path_strings)
    assert any("advertised-routes" in p for p in path_strings)
