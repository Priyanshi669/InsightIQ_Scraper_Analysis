import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

def cluster_reviews(csv_path="data/reviews.csv", k=3):
    df = pd.read_csv(csv_path)
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(df["review"])
    kmeans = KMeans(n_clusters=k, random_state=42)
    df["cluster"] = kmeans.fit_predict(X)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/reviews_clustered.csv", index=False)

    # plot cluster distribution
    cluster_counts = df["cluster"].value_counts().sort_index()
    cluster_counts.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Review Distribution by Cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    plt.savefig("data/cluster_distribution.png")
    print("✅ Clustered reviews saved and chart generated.")