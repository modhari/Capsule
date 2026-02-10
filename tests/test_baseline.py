from gnmi_collection_agent.core.baseline import BaselineStore


def test_detect_anomaly_none_until_min_updates():
    b = BaselineStore(window_size=10)
    key = "dev1"
    metric = "cpu"
    for _ in range(4):
        b.update(key, metric, 10.0)
    assert b.detect_anomaly(key, metric, 50.0, z_threshold=3.0, min_updates=5) is None


def test_detect_anomaly_spike():
    b = BaselineStore(window_size=50)
    key = "dev1"
    metric = "cpu"
    for _ in range(30):
        b.update(key, metric, 10.0)

    res = b.detect_anomaly(key, metric, 80.0, z_threshold=3.0, min_updates=10)
    assert res is not None

    mean, std, z = res
    assert mean == 10.0
    assert std > 0.0
    assert z > 0.0
