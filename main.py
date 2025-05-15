from flask import Flask, jsonify, render_template, request
from data import appDataBase
from core.usecase.user import Login, Signin, UpdateUser,ChangePassword
from core.usecase.machine import AddMachine, EnableMachine, DisableMachine
from core.usecase.categorie import AddCategorie, EnableCategorie, DisableCategorie
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

@app.route("/load_signin")
def load_signin():
    return render_template("singin.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    request_value = request.get_json()
    Signin.usecase_signing(
        dni=request_value.get("dni"), 
        password=request_value.get("password"),
        email=request_value.get("email"),
        name=request_value.get("name"),
        lastname=request_value.get("lastname"),
        employee_number=request_value.get("employee_number"),
        db=appDataBase
    )
    return "", 204

@app.route("/user/update_user", methods=["PUT"])
def update_user():
    request_value = request.get_json()
    UpdateUser.usecase_update_user(
        #email=request_value.get("email"),
        dni = request_value.get("dni"),
        name=request_value.get("name"),
        lastname=request_value.get("lastname"),
    )
    return "", 204

@app.route("/user/change_password", methods=["PUT"])
def change_password():
    request_value = request.get_json()
    ChangePassword(
        dni = request_value.get("dni"),
        password_Act = request_value.get("passwordAct"),
        password_New_1 = request_value.get("password1"),
        password_New_2 = request_value.get("password2")
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

@app.route("/machine/view_description", methods=["GET"])
def view_description():
    patent = request.args.get("patent")
    if not patent:
        return jsonify({"error": "No patent provided"}), 400
    

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