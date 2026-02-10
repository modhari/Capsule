from gnmi_collection_agent.core.types import CapabilityProfile, DeviceIdentity


def test_device_identity_constructs():
    d = DeviceIdentity(
        device_id="d1",
        vendor="arista",
        os_name="eos",
        model="7050",
        mgmt_address="10.0.0.1",
    )
    assert d.device_id == "d1"
    assert d.vendor == "arista"


def test_capability_profile_constructs():
    c = CapabilityProfile(
        device_id="d1",
        supports_openconfig=True,
        supported_models={"openconfig_system": "1.0"},
        origins={"openconfig": "openconfig"},
    )
    assert c.supports_openconfig is True
    assert "openconfig_system" in c.supported_models
