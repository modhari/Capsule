from gnmi_collection_agent.gnmi.capability import build_capability_profile


def test_capability_builder_detects_openconfig():
    models = {"openconfig_system": "1.0", "vendor_native": "9.9"}
    c = build_capability_profile(device_id="d1", models=models)
    assert c.supports_openconfig is True
    assert "openconfig" in c.origins


def test_capability_builder_without_openconfig():
    models = {"vendor_native": "9.9"}
    c = build_capability_profile(device_id="d1", models=models)
    assert c.supports_openconfig is False
    assert c.origins == {}
