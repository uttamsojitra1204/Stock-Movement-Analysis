# Stock Movement Analysis Based on Social Media Sentiment

This project uses sentiment analysis on Reddit stock posts to predict stock movement trends. The sentiment scores of the posts are used to train a machine learning model to predict whether stock prices will go up or down.

## Requirements
- Python 3.x
- Required libraries: `pandas`, `nltk`, `sklearn`, `praw`, `joblib`

## Steps to Run

1. **Set up Reddit API credentials:**
   - Go to the [Reddit Developer Console](https://www.reddit.com/prefs/apps) and create a new application to get `client_id`, `client_secret`, and `user_agent`.
   - Replace these credentials in `reddit_scraper.py`.

2. **Scrape Data from Reddit:**
   - Run `reddit_scraper.py` to scrape stock-related posts from Reddit. The scraped data will be saved as `reddit_stock_posts.csv`.

3. **Perform Sentiment Analysis:**
   - Run `sentiment_analysis.py` to perform sentiment analysis on the scraped data. It will add a sentiment score column and save the results in `reddit_stock_sentiment.csv`.

4. **Build and Evaluate the Prediction Model:**
   - Run `predict_stock_movement.py` to train a machine learning model on the sentiment data. The model will predict stock movements and evaluate the performance using accuracy and other metrics.

5. **Results:**
   - The model's accuracy and classification report will be printed after training.
   - The trained model will be saved as `stock_movement_model.pkl`.

## Future Improvements
- Integrating stock price data for more accurate prediction.
- Using more advanced machine learning models or deep learning approaches for better performance.

## Demo Video (Optional)
- A demo video can be provided to showcase the steps of the project.
