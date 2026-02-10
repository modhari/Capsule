from gnmi_collection_agent.gnmi.client import FakeGnmiClient, GnmiPath, GnmiUpdate


def test_fake_client_capabilities():
    c = FakeGnmiClient(models={"openconfig_system": "1.0"}, updates=[])
    caps = c.capabilities()
    assert "openconfig_system" in caps


def test_fake_client_get_filters_updates():
    p1 = GnmiPath(origin="openconfig", path="/system/cpu")
    p2 = GnmiPath(origin="openconfig", path="/interfaces/counters")

    u1 = GnmiUpdate(path=p1, ts_unix_s=1.0, value=10.0, labels={"device": "d1"})
    u2 = GnmiUpdate(path=p2, ts_unix_s=1.0, value=99.0, labels={"device": "d1"})

    c = FakeGnmiClient(models={}, updates=[u1, u2])
    res = c.get([p1])

    assert len(res) == 1
    assert res[0].path == p1
    assert c.get_calls == [("openconfig", "/system/cpu")]
