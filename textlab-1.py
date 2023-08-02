from textblob import TextBlob
from colors import *
def analyzer(text):
    blob = TextBlob(text)

    polaridad = blob.sentiment.polarity

    if polaridad > 0:
        tag = f"{G}Positivo - Positive"
    elif polaridad < 0:
        tag = f"{R}Negativo - Negative"
    else:
        tag = f"{W}Neutral"

    return tag


def main():
    text = input("Text(EN/ES): ")
    result = analyzer(text)

print(f"{G} FEEL {O}{result}")
