import pandas as pd
from transformers import pipeline
import os

def analyze_sentiment_with_bert(csv_path="data/reviews.csv"):
    print("🔍 Loading reviews...")
    df = pd.read_csv(csv_path)

    if "review" not in df.columns:
        raise ValueError("❌ 'review' column not found in the CSV.")

    print("🤖 Loading BERT sentiment pipeline...")
    classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    print("🧠 Classifying sentiment for each review...")
    sentiments = []
    for review in df["review"]:
        try:
            result = classifier(review[:512])[0]
            sentiments.append(result["label"])
        except Exception as e:
            sentiments.append("ERROR")
            print(f"⚠️ Failed on review: {review[:30]}... – {e}")

    df["bert_sentiment"] = sentiments
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/review_bert_sentiment.csv", index=False)
    print("✅ Saved to data/review_bert_sentiment.csv")
    return df