from __future__ import annotations

from gnmi_collection_agent.gnmi.client import GnmiPath


class OpenConfigPaths:
    """
    Central place for OpenConfig gNMI paths used across vendor packs.

    Why this exists:
    Keeping OpenConfig paths in one module prevents duplication across vendors
    and makes it easy to evolve paths over time while keeping vendor packs stable.

    Notes:
    These are intentionally minimal at first. We add more paths gradually as the project grows.
    """

    system_cpu_total = GnmiPath(
        origin="openconfig",
        path="/system/cpus/cpu/state/total/avg",
    )
