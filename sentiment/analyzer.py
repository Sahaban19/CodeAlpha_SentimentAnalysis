# analyzer.py
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# TextBlob Analysis
def analyze_textblob(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'
    return sentiment, polarity

# VADER Analysis
vader_analyzer = SentimentIntensityAnalyzer()

def analyze_vader(text):
    score = vader_analyzer.polarity_scores(text)["compound"]
    sentiment = 'positive' if score > 0.05 else 'negative' if score < -0.05 else 'neutral'
    return sentiment, score
