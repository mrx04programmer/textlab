from textblob import TextBlob
from colors import *
def analyzer(text):
    blob = TextBlob(text)

    polaridad = blob.sentiment.polarity

    if polaridad > 0:
        tag = "Positivo"
    elif polaridad < 0:
        tag = "Negativo"
    else:
        tag = "Neutral"

    return tag


def main():
    text = input("Texto: ")
    result = analyzer(text)

print(f"{G} FEEL {O}{result}")
