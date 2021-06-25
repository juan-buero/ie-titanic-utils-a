from flask import Flask, request
from ie_utils import tokenize

app = Flask(__name__) #to identify web app

@app.route("/") # decorator for function that URL corresponds to function. Link between function and URL
def home():
    return "Hello world!"

@app.route("/tokenize")
def do_tokenize():
    print(request.args)
    return str(tokenize("Hello world!"))