from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.vendors.arista import AristaPack
from gnmi_collection_agent.vendors.registry import VendorRegistry


def test_vendor_registry_picks_arista_pack():
    registry = VendorRegistry(packs=[AristaPack()])

    ident = DeviceIdentity(
        device_id="d1",
        vendor="arista",
        os_name="eos",
        model="7050",
        mgmt_address="10.0.0.1",
    )

    pack = registry.pick(ident)
    assert pack is not None
    assert pack.match(ident) is True


def test_vendor_registry_returns_none_for_unknown_vendor():
    registry = VendorRegistry(packs=[AristaPack()])

    ident = DeviceIdentity(
        device_id="d2",
        vendor="unknown",
        os_name="unknown",
        model="unknown",
        mgmt_address="10.0.0.2",
    )

    pack = registry.pick(ident)
    assert pack is None
