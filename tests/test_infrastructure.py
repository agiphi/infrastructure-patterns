from infrastructure_patterns.config import config
from infrastructure_patterns.health import health, readiness
from infrastructure_patterns.logging import event


def test_config_has_environment():
    assert config()["environment"]


def test_health_contract():
    result=health("test-service")
    assert result["status"] == "ok"
    assert result["service"] == "test-service"


def test_readiness_contract():
    assert readiness({"environment":"test"})
    assert not readiness({"environment":"unknown"})


def test_structured_event_is_json():
    assert '"event": "started"' in event("started", version="1")
