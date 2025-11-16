# Mock GeoIP database (offline)
# You can later replace this with MaxMind GeoIP lookup.

GEO_DATABASE = {
    "192.168.1.10": "Kazakhstan",
    "192.168.1.11": "Germany",
    "10.0.0.5": "Kazakhstan",
    "34.55.22.1": "USA"
}

def detect_impossible_travel(entries):
    last_location = {}
    alerts = []

    for e in entries:
        ip = e["ip"]
        country = GEO_DATABASE.get(ip, "Unknown")

        if e["type"] == "success":
            if ip in last_location:
                if last_location[ip] != country and country != "Unknown":
                    alerts.append({
                        "alert": "Impossible travel detected",
                        "ip": ip,
                        "from": last_location[ip],
                        "to": country,
                        "risk": "Medium"
                    })
            last_location[ip] = country

    return alerts
