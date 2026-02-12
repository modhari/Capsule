from __future__ import annotations

from typing import List

from gnmi_collection_agent.core.types import DeviceIdentity
from gnmi_collection_agent.gnmi.paths import OpenConfigPaths
from gnmi_collection_agent.vendors.base import SensorGroup, VendorPack


class CiscoPack(VendorPack):
    """
    CiscoPack defines the telemetry plan for Cisco devices.

    Today this pack starts minimal on purpose:
    1. It proves the vendor abstraction works
    2. It gives us a place to expand into IOS XR, NX OS, and platform specific fallbacks later

    Strategy:
    OpenConfig first whenever supported.
    Vendor native fallbacks will come later when we add more metrics that vary by platform.
    """

    def match(self, ident: DeviceIdentity) -> bool:
        # We match on the vendor string.
        # Later we can expand to also match based on os_name for cases like iosxr and nxos.
        return ident.vendor.lower() == "cisco"

    def sensor_groups(self, supports_openconfig: bool) -> List[SensorGroup]:
        """
        Return sensor groups for this vendor.

        A sensor group is a named bundle of telemetry paths with a sampling interval.
        This keeps subscribe plans modular and prevents one giant subscription stream.
        """
        if supports_openconfig:
            # Start with one high value metric to validate the pipeline.
            # CPU is universally useful and has low cardinality.
            return [
                SensorGroup(
                    name="system",
                    sample_interval_s=10.0,
                    paths=[OpenConfigPaths.system_cpu_total],
                )
            ]

        # When OpenConfig is not supported, we return empty for now.
        # A future commit will add vendor native paths for Cisco platforms.
        return []
