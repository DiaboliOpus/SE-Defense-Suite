def detect_bruteforce(entries):
    failures = {}

    for e in entries:
        if e["type"] == "failed":
            ip = e["ip"]
            failures[ip] = failures.get(ip, 0) + 1

    alerts = []
    for ip, count in failures.items():
        if count >= 3:
            alerts.append({
                "alert": "Brute-force detected",
                "ip": ip,
                "failures": count,
                "risk": "High"
            })

    return alerts
