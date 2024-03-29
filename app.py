import requests
from flask import Flask, request
import json
import os
from processing import downloadurl

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return os.environ['SECRET_KEY']
    if request.method == "POST":
        req_data = request.json
        url = req_data['url']
        result=downloadurl(url)
        return result

if __name__ == '__main__':
    app.run()