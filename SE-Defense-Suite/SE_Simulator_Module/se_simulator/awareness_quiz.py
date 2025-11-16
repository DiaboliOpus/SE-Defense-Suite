import json, random

QUIZ_PATH = "se_simulator/templates/quiz_templates.json"

def load_quiz_templates():
    with open(QUIZ_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_quiz(num_questions=5):
    templates = load_quiz_templates()["questions"]
    selected = random.sample(templates, num_questions)
    return selected

if __name__ == "__main__":
    print(generate_quiz())
