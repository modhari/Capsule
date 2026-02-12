from __future__ import annotations

from typing import List

from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.gnmi.paths import OpenConfigPaths
from gnmi_collection_agent.vendors.base import SensorGroup, VendorPack


class NokiaPack(VendorPack):
    """
    NokiaPack defines telemetry plans for Nokia SR OS devices.

    Nokia SR OS has strong model driven management support, and OpenConfig coverage depends on release.
    The pack starts with OpenConfig only, then we will add SR OS specific fallbacks as we extend scope.

    This staged approach keeps the commit history realistic and the code easy to review.
    """

    def match(self, ident: DeviceIdentity) -> bool:
        return ident.vendor.lower() == "nokia"

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
