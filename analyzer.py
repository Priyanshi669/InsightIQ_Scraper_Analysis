import pandas as pd
from textblob import TextBlob

def analyze_reviews(csv_path="data/reviews.csv"):
    df = pd.read_csv(csv_path)
    sentiments = []
    for text in df["review"]:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiments.append("Positive")
        elif polarity < 0:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")
    df["textblob_sentiment"] = sentiments
    df.to_csv(csv_path, index=False)
    print("✅ Added textblob sentiment to", csv_path)