import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Load scraped data from Reddit
df = pd.read_csv('reddit_stock_posts.csv')

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to calculate sentiment score
def get_sentiment(text):
    score = sia.polarity_scores(text)
    return score['compound']  # Compound score represents overall sentiment

# Apply sentiment analysis to posts
df['sentiment_score'] = df['post'].apply(get_sentiment)

# Save the sentiment-labeled data
df.to_csv('reddit_stock_sentiment.csv', index=False)

print("Sentiment analysis completed and saved to 'reddit_stock_sentiment.csv'")
