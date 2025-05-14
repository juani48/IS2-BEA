from flask import Flask, jsonify, render_template, request
from data import appDataBase
from core.usecase import Login, Singin
from core.usecase.machine import AddMachine
from core.usecase.categorie import AddCategorie
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
        db=appDataBase
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
        db=appDataBase
    )
    return "", 204

@app.route("/machine/add_machine", methods=["GET", "POST"])
def add_machine():
    request_value = request.get_json()
    AddMachine.usecase_add_machine(
        patent=request_value.get("patent"),
        mark=request_value.get("patent"),
        model=request_value.get("model"),
        price_day=request_value.get("price_day"),
        ubication=request_value.get("ubication"),
        refund=request_value.get("refund"),
        categorie=request_value.get("categorie")
    )
    return "", 204

@app.route("/categorie/add_categorie", methods=["GET", "POST"])
def add_categorie():
    request_value = request.get_json()
    AddCategorie.usecase_add_categorie(
        categorie=request_value.get("categorie")
    )
    return "", 204


if __name__ == '__main__':
    app.run(debug=True)
    appDataBase.create_database()