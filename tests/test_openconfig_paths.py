from gnmi_collection_agent.gnmi.paths import OpenConfigPaths


def test_openconfig_paths_cpu_exists():
    p = OpenConfigPaths.system_cpu_total
    assert p.origin == "openconfig"
    assert p.path.startswith("/")
