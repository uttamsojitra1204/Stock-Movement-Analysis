import praw
import pandas as pd

# Set up Reddit API credentials
client_id = 'eT-O4y8NQFIAKqLmpDTxeQ'
client_secret = 'JqZ8ZcP8n-wSgI3Vp4UjHKbdSH2Esg'
user_agent = 'StockScraper:v1.0 (by /u/uttamsojitra'

# Initialize Reddit API instance
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# Choose a subreddit related to stock market discussions (e.g., r/stocks or r/investing)
subreddit_name = 'stocks'
subreddit = reddit.subreddit(subreddit_name)

# List to hold scraped posts
posts = []

# Scrape the latest 100 posts from the selected subreddit
for post in subreddit.new(limit=100):
    posts.append([post.title, post.selftext])

# Convert the posts to a pandas DataFrame
df = pd.DataFrame(posts, columns=['title', 'post'])

# Save the data to a CSV file
df.to_csv('reddit_stock_posts.csv', index=False)

print("Data scraped and saved to 'reddit_stock_posts.csv'")
