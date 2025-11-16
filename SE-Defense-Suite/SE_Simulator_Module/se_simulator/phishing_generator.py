import json, random, datetime

TEMPLATE_PATH = "templates/phishing_templates.json"

def load_templates():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_phishing_email(difficulty="medium"):
    templates = load_templates()
    selected = random.choice(templates["templates"])
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    email = selected["template"]
    variables = {
        "{{DATE}}": now,
        "{{USERNAME}}": random.choice(["user", "employee", "colleague", "member"]),
        "{{COMPANY}}": random.choice(["Microsoft", "Google", "Meta", "Apple", "Amazon"]),
        "{{SERVICE}}": random.choice(["Office365", "Drive", "Cloud", "Mail"]),
        "{{AMOUNT}}": str(random.randint(100, 900)),
        "{{COUNTRY}}": random.choice(["Kazakhstan", "USA", "Germany", "France"]),
        "{{DEVICE}}": random.choice(["Windows PC", "iPhone 14", "Android device", "MacBook Pro"]),
    }

    for key, val in variables.items():
        email = email.replace(key, val)

    return {
        "subject": selected["subject"],
        "body": email,
        "difficulty": difficulty
    }

if __name__ == "__main__":
    print(generate_phishing_email())
