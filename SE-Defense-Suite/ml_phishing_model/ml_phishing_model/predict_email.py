import pickle
import re

MODEL_PATH = "phishing_classifier.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"


def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)
    return text.lower()


def predict(subject, body):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)

    combined = clean_text(subject + " " + body)
    features = vectorizer.transform([combined])

    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features).max()

    return prediction, round(confidence, 3)


if __name__ == "__main__":
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    label, confidence = predict(subject, body)
    print(f"Prediction: {label} (confidence: {confidence})")