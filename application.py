from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

def load_model():
    global loaded_model
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)
    
    global vectorizer
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)
    
    return


@app.route("/predict/<string:input>", methods=["GET"])
def predict(input):
    load_model()
    prediction = loaded_model.predict(vectorizer.transform([input]))[0]
    return prediction

if __name__ == "__main__":
    app.run()


