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


def test_arista_pack_does_not_match_other_vendor():
    p = AristaPack()
    ident = DeviceIdentity(
        device_id="d2",
        vendor="juniper",
        os_name="junos",
        model="mx480",
        mgmt_address="10.0.0.2",
    )
    assert p.match(ident) is False


def test_arista_pack_returns_empty_without_openconfig():
    p = AristaPack()
    groups = p.sensor_groups(supports_openconfig=False)
    assert groups == []


def test_arista_pack_returns_all_sensor_groups_when_openconfig_supported():
    p = AristaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    names = [g.name for g in groups]
    assert "system" in names
    assert "bgp_session" in names
    assert "bgp_prefixes" in names
    assert "bgp_topology" in names


def test_arista_pack_system_group_uses_openconfig():
    p = AristaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    system = next(g for g in groups if g.name == "system")
    assert all(path.origin == "openconfig" for path in system.paths)


def test_arista_pack_bgp_session_group_has_required_paths():
    p = AristaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    bgp = next(g for g in groups if g.name == "bgp_session")
    path_strings = [p.path for p in bgp.paths]
    assert any("session-state" in p for p in path_strings)
    assert any("last-error" in p for p in path_strings)
    assert any("peer-as" in p for p in path_strings)


def test_arista_pack_bgp_prefixes_group_has_required_paths():
    p = AristaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    prefixes = next(g for g in groups if g.name == "bgp_prefixes")
    path_strings = [p.path for p in prefixes.paths]
    assert any("received" in p for p in path_strings)
    assert any("sent" in p for p in path_strings)


def test_arista_pack_all_paths_use_openconfig_origin():
    p = AristaPack()
    groups = p.sensor_groups(supports_openconfig=True)
    for group in groups:
        for path in group.paths:
            assert path.origin == "openconfig", (
                f"Expected openconfig origin for path {path.path} "
                f"in group {group.name}"
            )
