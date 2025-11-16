import re
import tldextract
import json

SUSPICIOUS_TLDS = ["zip","xyz","top","click","country","kim","science","work"]
PHISHING_KEYWORDS = ["login","verify","update","secure","account","bank","signin","reset"]

def analyze_url(url: str):
    report = {"url": url, "flags": []}

    # Rule 1: @ symbol obfuscation
    if "@" in url:
        report["flags"].append("Contains '@' (redirect obfuscation)")

    # Rule 2: Suspicious TLD
    ext = tldextract.extract(url)
    if ext.suffix in SUSPICIOUS_TLDS:
        report["flags"].append(f"Suspicious TLD: .{ext.suffix}")

    # Rule 3: Phishing keywords in path
    for kw in PHISHING_KEYWORDS:
        if kw in url.lower():
            report["flags"].append(f"Contains phishing keyword: '{kw}'")

    # Rule 4: Excessive subdomains
    if len(ext.subdomain.split(".")) >= 3:
        report["flags"].append("Excessive subdomains (possible misdirection)")

    # Rule 5: IP-address URL
    if re.match(r'^https?://\d+\.\d+\.\d+\.\d+', url):
        report["flags"].append("Uses raw IP instead of domain")

    # Assign risk level
    score = len(report["flags"])
    if score == 0:
        report["risk"] = "Low"
    elif score <= 2:
        report["risk"] = "Medium"
    else:
        report["risk"] = "High"

    return report

if __name__ == "__main__":
    test = input("Enter URL to analyze: ")
    print(json.dumps(analyze_url(test), indent=4))
