import json

with open("templates/controls_reference.json") as f:
    CONTROLS = json.load(f)

def get_controls(category):
    return CONTROLS.get(category, [])

if __name__ == "__main__":
    print(get_controls("Phishing"))
