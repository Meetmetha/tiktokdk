import requests
from flask import Flask, request
from flask import jsonify
import json
import os
from processing import downloadurl

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return "Follow POST Request with URL param"
    if request.method == "POST":
        req_data = request.json
        url = req_data['url']
        result=downloadurl(url)
        return result

if __name__ == '__main__':
    app.run()