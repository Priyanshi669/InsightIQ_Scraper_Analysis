import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="InsightIQ Dashboard", layout="wide")
st.title("📊 InsightIQ Dashboard")

try:
    df = pd.read_csv("data/reviews_clustered.csv")
except FileNotFoundError:
    st.error("❌ reviews_clustered.csv not found. Run the pipeline first.")
    st.stop()

# Show raw data
with st.expander("📋 Raw Data"):
    st.dataframe(df)

# Cluster Distribution
st.subheader("📈 Cluster Distribution")
fig, ax = plt.subplots()
df["cluster"].value_counts().sort_index().plot(kind="bar", ax=ax, color="orange")
ax.set_title("Number of Reviews per Cluster")
ax.set_xlabel("Cluster")
ax.set_ylabel("Count")
st.pyplot(fig)

# BERT Sentiment Breakdown
if "bert_sentiment" in df.columns:
    st.subheader("🧠 BERT Sentiment Analysis")
    st.bar_chart(df["bert_sentiment"].value_counts())
else:
    st.warning("⚠️ BERT sentiment column not found.")