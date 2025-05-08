from flask import Flask, jsonify, render_template, request
from data import config 
from flask_sqlalchemy import SQLAlchemy
from templates import *

app = Flask(__name__)	

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/singin", methods=["GET", "POST"])
def login():
    request_value = request.get_json()
    print(request_value.get("name"))
    return "", 204    

if __name__ == '__main__':
    app.run(debug=True)