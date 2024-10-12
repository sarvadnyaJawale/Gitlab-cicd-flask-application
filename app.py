from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def main():
    return "WELCOME TO MY WEBSITE : ~HARSH"

app.run(host='0.0.0.0', port=8080)
