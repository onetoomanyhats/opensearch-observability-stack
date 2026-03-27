import argparse
import json
import random
from datetime import datetime
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--events", type=int, default=1000)
args = parser.parse_args()

log_file = Path("logs/app.log")
log_file.parent.mkdir(parents=True, exist_ok=True)

services = ["api", "worker", "scheduler", "auth"]

with log_file.open("a", encoding="utf-8") as f:
    for _ in range(args.events):
        event = {
            "@timestamp": datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
            "service": random.choice(services),
            "level": "ERROR" if random.random() < 0.15 else "INFO",
            "status_code": 500 if random.random() < 0.10 else 200,
            "latency_ms": random.randint(20, 5000),
            "request_id": f"burst-{random.randint(100000, 999999)}",
            "message": "Burst traffic event",
            "host": "demo-node-burst"
        }
        f.write(json.dumps(event) + "\n")

print(f"Wrote {args.events} burst events to {log_file}")
