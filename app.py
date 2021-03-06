from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__) #to identify web app

@app.route("/") # decorator for function that URL corresponds to function. Link between function and URL
def home():
    return {
        "message": "Hello world!",
        "version": "0.1",
    }

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    sentence = request.args["sentence"]
    lower = bool(request.args.get("lower", False))
    return str(tokenize(sentence, lower=lower))