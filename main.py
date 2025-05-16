from flask import Flask, jsonify, render_template, request
from data import appDataBase
from core.usecase import Login, Singin
from core.usecase.machine import AddMachine, EnableMachine, DisableMachine, GetAllMachines, GetAllMachinesByFilter, GetAllMachinesByName
from core.usecase.categorie import AddCategorie, EnableCategorie, DisableCategorie
from templates import *

app = Flask(__name__)	

@app.route('/')
def home():
    return render_template('/main.html')

# ---- RENDERIZAR PAGINAS ---- #

@app.route('/main.html')
def load_home():
    return render_template('/main.html')

@app.route('/machinery.html')
def load_machinery():
    return render_template('/machinery.html')

@app.route("/login.html")
def load_login():
    return render_template("/login.html")

@app.route("/singin.html")
def load_singin():
    return render_template("singin.html")

@app.route("/reserve.html")
def load_reserve():
    return render_template("/reserve.html")

# ---- METODOS POST ---- #

@app.route("/login", methods=["GET", "POST"])
def Login():
    request_value = request.get_json()
    Login.usecase_login(
        dni=request_value.get("dni"), 
        password=request_value.get("password"),
        db=appDataBase
    )
    return "", 204

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

# ---- Maquinas ----

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

@app.route("/machine/enable_machine", methods=["GET", "POST"])
def enable_machine():
    request_value = request.get_json().get("patent")
    EnableMachine.usecase_enable_machine(patent=request_value)
    return "", 204

@app.route("/machine/disable_machine", methods=["GET", "POST"])
def disable_machine():
    request_value = request.get_json().get("patent")
    DisableMachine.usecase_disable_machine(patent=request_value)
    return "", 204

@app.route("/machine/get_all", methods=["GET", "POST"])
def get_all_machines():
    request.get_json()
    return jsonify( GetAllMachines.usecase_get_all_machines() ), 200 # verfificar si e snecesario el jsonify

@app.route("/machine/get_all_name", methods=["GET", "POST"])
def get_all_machines_name():
    request_value = request.get_json().get("name")
    return jsonify(
        GetAllMachinesByName.usecase_get_all_machines_by(name=request_value)
    ), 200

@app.route("/machine/get_all_filter", methods=["GET", "POST"])
def get_all_machines_filter():
    return GetAllMachinesByFilter.usecase_get_all_machines_by( 
        categorie_filter=request.get_json().get("categoire"),
        price_filter=request.get_json().get("price"),
        mark_filter=request.get_json().get("mark"),
        model_filter=request.get_json().get("model")), 200
    # json del request = { "categorie": { "apply": Bool, "categorie": "string" }, ... }

# ---- Categorias ----

@app.route("/categorie/add_categorie", methods=["GET", "POST"])
def add_categorie():
    request_value = request.get_json()
    AddCategorie.usecase_add_categorie(
        categorie=request_value.get("categorie")
    )
    return "", 204

@app.route("/categorie/enable_categorie", methods=["GET", "POST"])
def enable_categorie():
    request_value = request.get_json().get("categorie")
    EnableCategorie.usecase_enable_categorie(categorie=request_value)
    return "", 204

@app.route("/categorie/disable_categorie", methods=["GET", "POST"])
def disable_categorie():
    request_value = request.get_json().get("categorie")
    DisableCategorie.usecase_disable_categorie(categorie=request_value)
    return "", 204


# --- MAIN ----

if __name__ == '__main__':
    app.run(debug=True)
    appDataBase.create_database()
    