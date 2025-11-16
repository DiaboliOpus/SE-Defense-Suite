import json

RISK_LEVELS = [
    ["Low", "Low", "Medium", "Medium", "High"],
    ["Low", "Medium", "Medium", "High", "High"],
    ["Medium", "Medium", "High", "High", "Critical"],
    ["Medium", "High", "High", "Critical", "Critical"],
    ["High", "High", "Critical", "Critical", "Critical"]
]

def generate_risk_matrix(likelihood, impact):
    return RISK_LEVELS[likelihood-1][impact-1]

if __name__ == '__main__':
    print(generate_risk_matrix(5,5))
