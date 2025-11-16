import pandas as pd
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

DATASET_PATH = "data/sample_dataset.csv"
MODEL_PATH = "phishing_classifier.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"
METRICS_PATH = "evaluation/metrics.txt"


def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9 ]", " ", text)
    return text.lower()


def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    df["combined"] = (df["subject"] + " " + df["body"]).apply(clean_text)
    return df


def train_model():
    df = load_dataset()
    X = df["combined"]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train_tfidf, y_train)

    predictions = model.predict(X_test_tfidf)
    report = classification_report(y_test, predictions)

    with open(METRICS_PATH, "w") as f:
        f.write(report)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

    print("Training complete.")


if __name__ == "__main__":
    train_model()