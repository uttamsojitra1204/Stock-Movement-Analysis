import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load sentiment-labeled data
df = pd.read_csv('reddit_stock_sentiment.csv')

# Assuming the sentiment score is a good indicator for stock movement prediction
# In reality, you'd have stock price data to correlate with sentiment scores.

# For demonstration, create a mock stock movement column (1 = Up, 0 = Down)
df['stock_movement'] = df['sentiment_score'].apply(lambda x: 1 if x > 0 else 0)

# Feature extraction (use sentiment_score as a feature for simplicity)
X = df[['sentiment_score']]  # Features
y = df['stock_movement']     # Target variable (stock movement: 1 = Up, 0 = Down)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model using RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict stock movements
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'stock_movement_model.pkl')
print("Model saved as 'stock_movement_model.pkl'")
