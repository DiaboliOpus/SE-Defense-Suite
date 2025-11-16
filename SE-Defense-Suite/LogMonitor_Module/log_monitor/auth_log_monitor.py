import re
import json
from datetime import datetime
from brute_force_detector import detect_bruteforce
from geoip_helper import detect_impossible_travel

LOG_PATH = "sample_logins.log"

def parse_log_line(line):
    failed = re.search(r"Failed login from (\d+\.\d+\.\d+\.\d+)", line)
    success = re.search(r"Successful login from (\d+\.\d+\.\d+\.\d+)", line)

    if failed:
        return {"type": "failed", "ip": failed.group(1), "raw": line}
    if success:
        return {"type": "success", "ip": success.group(1), "raw": line}
    return None

def monitor_logs():
    print("[SE-DEFENSE] Monitoring logs...")
    entries = []

    with open(LOG_PATH, "r") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                entries.append(parsed)

    alerts = []
    alerts.extend(detect_bruteforce(entries))
    alerts.extend(detect_impossible_travel(entries))

    print(json.dumps(alerts, indent=4))
    return alerts

if __name__ == "__main__":
    monitor_logs()
