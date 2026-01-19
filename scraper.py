import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def scrape_reviews():
    print("🕸️ Scraping dummy reviews...")
    sample_data = {
        "review": [
            "The product was great and delivered on time.",
            "Worst experience ever! Late delivery and rude support.",
            "Loved it! Will buy again.",
            "Not satisfied. The item was broken.",
            "Excellent service and quality."
        ]
    }
    df = pd.DataFrame(sample_data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/reviews.csv", index=False)
    print("✅ Reviews saved to data/reviews.csv")