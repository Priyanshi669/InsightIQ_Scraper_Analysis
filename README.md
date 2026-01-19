# InsightIQ_Scraper_Analysis
# InsightIQ: Review Scraper and Analysis Pipeline

InsightIQ is an end-to-end pipeline for scraping product reviews, performing sentiment analysis using both traditional (TextBlob) and advanced (BERT) methods, clustering reviews for insights, and visualizing results through an interactive Streamlit dashboard.

## Features

- **Web Scraping**: Scrapes reviews from websites (currently uses dummy data for demonstration).
- **Sentiment Analysis**:
  - TextBlob for basic polarity-based sentiment.
  - BERT (DistilBERT) for advanced sentiment classification.
- **Review Clustering**: Groups similar reviews using TF-IDF vectorization and K-Means clustering.
- **Interactive Dashboard**: Visualize cluster distributions, sentiment breakdowns, and raw data using Streamlit.
- **Modular Design**: Easy to extend and customize for different data sources.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyanshi669/InsightIQ_Scraper_Analysis.git
   cd InsightIQ_Scraper_Analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the full pipeline:
   ```bash
   python main.py
   ```
   This will scrape reviews, analyze sentiments, cluster them, and save results to the `data/` folder.

2. Launch the dashboard:
   ```bash
   streamlit run dashboard.py
   ```
   Open the provided URL in your browser to explore the visualizations.

## Project Structure

```
InsightIQ_Scraper_Analysis/
├── main.py                 # Main pipeline script
├── scraper.py              # Review scraping module
├── analyzer.py             # TextBlob sentiment analysis
├── bert_sentiment.py       # BERT sentiment analysis
├── cluster_reviews.py      # Review clustering with K-Means
├── dashboard.py            # Streamlit dashboard
├── requirements.txt        # Python dependencies
├── data/                   # Output data and visualizations
└── README.md               # This file
```

## Output Files

- `data/reviews.csv`: Raw scraped reviews.
- `data/review_bert_sentiment.csv`: Reviews with BERT sentiment labels.
- `data/reviews_clustered.csv`: Reviews with cluster assignments.
- `data/cluster_distribution.png`: Bar chart of cluster distribution.

## Customization

- **Scraping**: Modify `scraper.py` to scrape from real websites (ensure compliance with terms of service).
- **Clustering**: Adjust the number of clusters in `cluster_reviews.py` by changing the `k` parameter.
- **Models**: Swap BERT models in `bert_sentiment.py` for different languages or domains.

## Requirements

- Python 3.8+
- Internet connection for downloading BERT models (first run only)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is open-source. Feel free to use and modify as needed.
