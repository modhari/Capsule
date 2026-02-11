from __future__ import annotations

from typing import List

from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.gnmi.paths import OpenConfigPaths
from gnmi_collection_agent.vendors.base import SensorGroup, VendorPack


class AristaPack(VendorPack):
    def match(self, ident: DeviceIdentity) -> bool:
        return ident.vendor.lower() == "arista"

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
