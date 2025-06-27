# streamlit_app.py
import streamlit as st
from sentiment.analyzer import analyze_vader
from sentiment.emotion_detector import detect_emotions

st.title("Sentiment & Emotion Analyzer")

user_input = st.text_area("Enter your review or comment:")

if st.button("Analyze"):
    sentiment, score = analyze_vader(user_input)
    emotions = detect_emotions(user_input)
    st.write(f"Sentiment: {sentiment} (Score: {score})")
    st.write("Top Emotions:", emotions)
