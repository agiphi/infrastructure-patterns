from datetime import datetime, timezone

def health(service="reference-service"):
    return {"status":"ok","service":service,"timestamp":datetime.now(timezone.utc).isoformat()}

def readiness(config):
    return config.get("environment") in {"development","test","production"}
