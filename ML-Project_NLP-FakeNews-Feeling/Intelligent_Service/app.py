from flask import Flask, jsonify, request
from flask_cors import CORS
from NLP import nlp
from FakeNews import fakeNews
from Feeling import feeling

fakeNews.dataPreparation()
fakeNews.trainModel()

app = Flask(__name__)
CORS(app)

@app.route("/tokenizationSentence", methods=["POST"])
def tokenizationSentence():
    request_data = request.get_json()
    return jsonify(sentences=nlp.tokenizationSentence(request_data['text']))

@app.route("/tokenizationWord", methods=["POST"])
def tokenizationWord():
    request_data = request.get_json()
    return jsonify(words=nlp.tokenizationWord(nlp.removePunctuation(request_data['text'])))

@app.route("/wordsFrequency", methods=["POST"])
def wordsFrequency():
    request_data = request.get_json()
    return jsonify(wordsFq=nlp.wordsFrequency(nlp.removePunctuation(request_data['text']),request_data['nbr']))

@app.route("/removePunctiation", methods=["POST"])
def removePunction():
    request_data = request.get_json()
    return jsonify(text=nlp.removePunctuation(request_data['text']))

@app.route("/cleanText", methods=["POST"])
def cleanText():
    request_data = request.get_json()
    return jsonify(text=nlp.cleanText(request_data['text']))

@app.route("/stemming", methods=["POST"])
def stemming():
    request_data = request.get_json()
    return jsonify(text=nlp.stemming(request_data['text']))

@app.route("/lemmatization", methods=["POST"])
def lemmatization():
    request_data = request.get_json()
    return jsonify(text=nlp.lemmatization(request_data['text']))

@app.route("/posTagging", methods=["POST"])
def posTagging():
    request_data = request.get_json()
    return jsonify(tags=nlp.posTagging(request_data['text']))

@app.route("/bagOfWords", methods=["POST"])
def bagOfWords():
    request_data = request.get_json()
    sentences = nlp.tokenizationSentence(request_data['text'])
    sent = []
    for s in sentences:
        sent.append(nlp.lemmatization(nlp.cleanText(s)))
    return jsonify(bagOfWords=str(nlp.bagOfWords(sent)).replace('\t',' ').splitlines())

@app.route("/tfidf", methods=["POST"])
def tfidf():
    request_data = request.get_json()
    sentences = nlp.tokenizationSentence(request_data['text'])
    sent = []
    for s in sentences:
        sent.append(nlp.lemmatization(nlp.cleanText(s)))
    return jsonify(tfidf=str(nlp.tfidf(nlp.bagOfWords(sent))).replace('\t',' ').splitlines())

@app.route("/w2vSimilarity", methods=["POST"])
def w2vSimilarity():
    request_data = request.get_json()
    return jsonify(similarity=str(nlp.w2vSimilarity(request_data['word1'],request_data['word2'])))

@app.route("/detectFakeNews", methods=["POST"])
def detectFakeNews():
    request_data = request.get_json()
    pProb,pClass = fakeNews.detectFakeNews(request_data['text'])
    pTrue = 0
    pFalse = 0
    for tab in pProb:
        pTrue += tab[1]
        pFalse += tab[0]
    pProb = [pFalse/len(pProb), pTrue/len(pProb)]
    if(pProb[1]>=0.5):
        pClass = 1
    else:
        pClass = 0
    return jsonify(probability=pProb, pClass=pClass)

@app.route("/feeling", methods=["POST"])
def feelings():
    request_data = request.get_json()
    return jsonify(feeling=feeling.feeling(request_data['text']))