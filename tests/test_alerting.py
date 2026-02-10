from gnmi_collection_agent.core.alerting import AlertEngine
from gnmi_collection_agent.core.baseline import BaselineStore
from gnmi_collection_agent.core.severity import Severity


def test_alert_engine_emits_alert():
    baseline = BaselineStore(window_size=50)
    engine = AlertEngine(baseline=baseline)

    key = "dev1"
    metric = "drops"
    for _ in range(25):
        baseline.update(key, metric, 1.0)

    a = engine.anomaly_alert(
        key=key,
        metric=metric,
        value=100.0,
        z_threshold=3.0,
        min_updates=10,
        labels={"device": "dev1"},
        alert_name="drops_anomaly",
        severity=Severity.critical,
    )

    assert a is not None
    assert a.alert_name == "drops_anomaly"
    assert a.severity == Severity.critical
    assert a.labels["device"] == "dev1"
    assert "z" in a.evidence
