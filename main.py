from flask import Flask, jsonify, render_template, request
from data import AppDataBase
from core.usecase import Login, Singin
# from flask_sqlalchemy import SQLAlchemy
from templates import *

app = Flask(__name__)	

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/load_login")
def load_login():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def Login():
    request_value = request.get_json()
    Login.usecase_login(
        dni=request_value.get("dni"), 
        password=request_value.get("password"),
        db=AppDataBase
    )
    return "", 204

@app.route("/load_singin")
def load_singin():
    return render_template("singin.html")

@app.route("/singin", methods=["GET", "POST"])
def singin():
    request_value = request.get_json()
    Singin.usecase_singing(
        dni=request_value.get("dni"), 
        password=request_value.get("password"),
        email=request_value.get("email"),
        name=request_value.get("name"),
        lastname=request_value.get("lastname"),
        employee_number=request_value.get("employee_number"),
        db=AppDataBase
    )
    return "", 204


if __name__ == '__main__':
    app.run(debug=True)
    AppDataBase.create_database()