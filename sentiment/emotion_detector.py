# emotion_detector.py
from nrclex import NRCLex

def detect_emotions(text):
    emotions = NRCLex(text)
    return emotions.top_emotions
