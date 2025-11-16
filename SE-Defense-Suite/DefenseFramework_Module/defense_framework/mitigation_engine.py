import json

with open("templates/mitigation_reference.json") as f:
    MITIGATION = json.load(f)

def get_mitigation(method):
    return MITIGATION.get(method, [])

if __name__ == "__main__":
    print(get_mitigation("Pretexting"))
