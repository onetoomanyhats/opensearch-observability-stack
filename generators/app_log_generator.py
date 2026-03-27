import json
import random
import time
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/app.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

services = ["api", "worker", "scheduler", "auth"]
levels = ["INFO", "WARN", "ERROR"]
status_codes = [200, 200, 200, 201, 400, 401, 404, 500, 502]

def make_event():
    service = random.choice(services)
    status_code = random.choice(status_codes)
    latency_ms = random.randint(5, 2500)

    return {
        "@timestamp": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
        "service": service,
        "level": "ERROR" if status_code >= 500 else random.choice(levels),
        "status_code": status_code,
        "latency_ms": latency_ms,
        "request_id": f"req-{random.randint(100000, 999999)}",
        "message": f"{service} handled request with status {status_code}",
        "host": "demo-node-1"
    }

while True:
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(make_event()) + "\n")
    time.sleep(0.1)
