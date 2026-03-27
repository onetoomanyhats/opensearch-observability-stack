import json
import random
import time
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/app.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

levels = ["INFO", "WARN", "ERROR"]
services = ["api", "worker", "scheduler", "auth"]

while True:
    event = {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "level": random.choice(levels),
        "service": random.choice(services),
        "latency_ms": random.randint(10, 2500),
        "message": "Synthetic application log event",
        "request_id": f"req-{random.randint(100000, 999999)}"
    }
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
    time.sleep(0.2)
