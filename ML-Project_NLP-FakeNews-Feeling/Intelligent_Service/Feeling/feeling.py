from textblob import TextBlob

def feeling(text):
    blob = TextBlob(text)
    return blob.sentiment
