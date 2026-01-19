from scraper import scrape_reviews
from analyzer import analyze_reviews
from cluster_reviews import cluster_reviews
from bert_sentiment import analyze_sentiment_with_bert

def main():
    print("🚀 Starting InsightIQ Pipeline...")

    scrape_reviews()
    analyze_reviews()
    analyze_sentiment_with_bert(csv_path="data/reviews.csv")
    cluster_reviews(csv_path="data/reviews.csv")

    print("✅ InsightIQ pipeline completed.")

if __name__ == "__main__":
    main()