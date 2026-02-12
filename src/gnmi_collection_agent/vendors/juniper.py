from __future__ import annotations

from typing import List

from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.gnmi.paths import OpenConfigPaths
from gnmi_collection_agent.vendors.base import SensorGroup, VendorPack


class JuniperPack(VendorPack):
    """
    JuniperPack defines telemetry plans for Juniper devices.

    Why a separate pack:
    Junos often has different vendor native schemas and different coverage levels for OpenConfig.
    Keeping Juniper logic isolated prevents vendor quirks from leaking into common code.

    Initial scope:
    Only system CPU via OpenConfig, mirroring other vendors for parity.
    """

    def match(self, ident: DeviceIdentity) -> bool:
        return ident.vendor.lower() == "juniper"

    def sensor_groups(self, supports_openconfig: bool) -> List[SensorGroup]:
        if supports_openconfig:
            return [
                SensorGroup(
                    name="system",
                    sample_interval_s=10.0,
                    paths=[OpenConfigPaths.system_cpu_total],
                )
            ]
        return []
