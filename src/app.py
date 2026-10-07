import json
import os
from datetime import datetime, timezone


def config() -> dict:
    return {
        "environment": os.getenv("APP_ENV", "development"),
        "service": os.getenv("SERVICE_NAME", "reference-service"),
    }


def health() -> dict:
    return {
        "status": "ok",
        "service": config()["service"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def log_event(event: str, **fields) -> None:
    record = {"event": event, **fields}
    print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    log_event("service_start", **config())
    print(json.dumps(health(), indent=2))
