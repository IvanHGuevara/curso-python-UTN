from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola curso de Python de La UES!"

@app.route("/holis")
def holis():
    return "{'edad': 19}"

@app.route("/holux")
def holux():
    return "holuuuuuuxxxxxxxxxx"