import os
import datetime
import hashlib
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def readJSON():
    filename = os.path.join(app.static_folder, 'values.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
    return data

def writeJSON(data):
    filename = os.path.join(app.static_folder, 'values.json')
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/reception")
def reception():
    return render_template("reception.html")

@app.route("/getValues")
def getValues():
    data = readJSON()
    return jsonify(data)

@app.route("/sendValues/<rdata>")
def sendValues(rdata):
    data = readJSON()
    data[rdata.split("_")[0]] = int(rdata.split("_")[1])
    writeJSON(data)
    return jsonify(data)

def resetValues():
    data = readJSON()
    for i in data.keys():
        data[i] = 0
    writeJSON(data)

if __name__ == "__main__":
    resetValues()
    app.run(debug=True, host="0.0.0.0")