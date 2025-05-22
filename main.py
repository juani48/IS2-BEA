from flask import Flask, jsonify, render_template, request
from data import appDataBase
from core.usecase.user import Login, Signin, UpdateUser,ChangePassword
from core.usecase.machine import AddMachine, EnableMachine, DisableMachine, GetAllMachines, GetAllMachinesByFilter, GetAllMachinesByName
from core.usecase.categorie import AddCategorie, EnableCategorie, DisableCategorie
from templates import *
import os
from werkzeug.utils import secure_filename
from flask import redirect, url_for
from flask import flash



app = Flask(__name__)
app.secret_key = 'B3bQh7#2d@xZ!59sP0mT&vL'
UPLOAD_FOLDER = 'static/image/users'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)	

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
    return render_template("login.html")



@app.route("/reserve.html")
def load_reserve():
    return render_template("/reserve.html")

@app.route("/singin.html")
def load_singin():
    return render_template("/singin.html")

@app.route("/panelUsuario.html")
def load_panelUsuario():
    return render_template("/panelUsuario.html")

# ---- METODOS POST ---- #

@app.route("/login", methods=["POST"])
def Logins():
    dni = request.form["usuario"]
    password = request.form["password"]

    Login.usecase_login(
        dni=dni,
        password=password,
        db=appDataBase
    )
    return redirect(url_for("load_panelUsuario"))
    #return "exito en inicio de sesión",204 # o return "", 204 si usás JS



@app.route("/signin", methods=["POST"])
def signin():
    dni = request.form['dni']
    password = request.form['password']
    email = request.form['email']
    name = request.form['name']
    lastname = request.form['lastname']
    #employee_number = request.form['employee_number'] numero de empleado???
    dni_photo = request.files['dni_photo']  # ← nombre del campo en el HTML


    # Ejecutar lógica de registro
    try:
        Signin.usecase_signing(
            dni=dni,
            password=password, #no deberia ir
            email=email,
            name=name,
            lastname=lastname,
            employee_number=80,
            db=appDataBase
        )
    except Exception as e: 
        flash(str(e))  # Manda el mensaje de error al template
        return redirect(url_for("load_singin"))

    # Guardar imagen
    if dni_photo:
        filename = secure_filename(f"{dni}_{lastname}.jpg") # Se guarda la imagen con el dni y el apellido 
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        dni_photo.save(filepath)
    flash("Solicitud enviada. Tu cuenta está pendiente de confirmación.")
    return redirect(url_for("load_login"))

#@app.route("/signin", methods=["GET", "POST"])
#def signin():
#   request_value = request.get_json()
#  Signin.usecase_signing(
#     dni=request_value.get("dni"), 
#       password=request_value.get("password"),
#        email=request_value.get("email"),
#        name=request_value.get("name"),
#        lastname=request_value.get("lastname"),
#        employee_number=request_value.get("employee_number"),
#        db=appDataBase
#    )
#    return "", 204

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

@app.route("/machine/get_all", methods=["GET"])
def get_all_machines():
    return jsonify( { "value" : GetAllMachines.usecase_get_all_machines()} ), 200 # verfificar si e snecesario el jsonify

@app.route("/machine/get_all_name", methods=["GET", "POST"])
def get_all_machines_name():
    request_value = request.get_json().get("name")
    return jsonify(GetAllMachinesByName.usecase_get_all_machines_by(name=request_value)), 200

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

@app.route("/testMachine" ,methods=["GET"])
def chargemachine():
    AddMachine.usecase_add_machine(12345, "raptor", "700", 200, "la plata", 10, "categoria1")
    return "",204


# --- MAIN ----

if __name__ == '__main__':
    app.run(debug=True)
    appDataBase.create_database()
    
