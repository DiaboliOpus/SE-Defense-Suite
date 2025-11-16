# Log Monitor & Brute-Force Detector

This module detects:
- Failed login brute-force attacks
- Suspicious login patterns
- Impossible travel using mock geoIP lookup

## Files
- auth_log_monitor.py — main log parser
- brute_force_detector.py — detects repeated failed logins
- geoip_helper.py — detects impossible travel
- sample_logins.log — test input file

## Run:
```
python auth_log_monitor.py
```

Alerts will be printed in JSON format.
