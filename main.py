from datetime import datetime, timedelta
import json
from flask import Flask, jsonify, render_template, request, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from core.entity import User
from data.appDataBase import get_user
from flask import redirect # redirigir a mercado pago
from core.service.mercado_pago import PayByMercadoPago
from data import appDataBase
from core.usecase.user import Auth, UpdateUser,ChangePassword,RequestUser,AddEmployee
from core.usecase.machine import AddMachine, EnableMachine, DisableMachine, GetAllMachines, GetAllMachinesByFilter
from core.usecase.categorie import AddCategorie, EnableCategorie, DisableCategorie, GetAllCategories
from core.usecase.reserve import MachineReservations, AddReservation
from templates import *
import os
from werkzeug.utils import secure_filename
from flask import redirect, url_for
from flask import flash



app = Flask(__name__)

app.secret_key = 'B3bQh7#2d@xZ!59sP0mT&vL'
UPLOAD_FOLDER_USER = 'static/image/users'
app.config['UPLOAD_FOLDER_USER'] = UPLOAD_FOLDER_USER
os.makedirs(UPLOAD_FOLDER_USER, exist_ok=True)	

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER_MACHINE = 'static/image/machine'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
os.makedirs(UPLOAD_FOLDER_MACHINE, exist_ok=True)  # crea la carpeta si no existe
app.config['UPLOAD_FOLDER_MACHINE'] = UPLOAD_FOLDER_MACHINE

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'load_login'  # Redirección si el usuario no está logueado

@login_manager.user_loader
def load_user(user_id):
    user_model = get_user(user_id)
    return User(user_model) if user_model else None



@app.route('/')
def home():
    #AddCategorie.usecase_add_categorie("categoria1")
    #AddCategorie.usecase_add_categorie("categoria2")
    #AddMachine.usecase_add_machine("A", "marcaA", "modeloA", 10, "ubicacionA", 10, "categoria1", "", "")
    #AddMachine.usecase_add_machine("B", "marcaB", "modeloB", 4, "ubicacionB", 30, "categoria1", "", "")
    #AddMachine.usecase_add_machine("C", "marcaC", "modeloC", 10, "ubicacionC", 15, "categoria2", "", "")
    # GetAllMachinesByFilter.usecase_get_all_machines_by(categorie_filter={"apply": True, "categorie": "categoria1"}, string_filer=request.get_json().get("string"),price_filter=request.get_json().get("price"),            mark_filter=request.get_json().get("mark"),            model_filter=request.get_json().get("model"))

    # prueba de reservas
    # now = datetime.now(); date1 = now + timedelta(days=1); date1_1 = now + timedelta(days=2); date2 = now + timedelta(days=3); date2_1 = now + timedelta(days=4)
    
    #AddReservation.usecase_add_reserve(date1, date1_1, 1, "A1", 0, False)
    #AddReservation.usecase_add_reserve(date2, date2_1, 1, "A1", 0, False)
    #print({"value" : MachineReservations.usecase_get_all_reservations_by_machine("A1")})

    return render_template('/main.html')

# ---- RENDERIZAR PAGINAS ---- #

@app.route('/main.html')
def load_home():
    return render_template('/main.html')


@app.route('/machinery.html')
def load_machinery():
    machines = GetAllMachines.usecase_get_all_machines()  # obtiene todas las máquinas activas
    return render_template('machinery.html', machines=machines)


#@app.route("/login.html")
#def load_login():
#    return render_template("login.html")

from flask import request, session, jsonify, redirect
from core.usecase.user.Auth import usecase_login

@app.route("/login", methods=["POST"])
def login_route():
    try:
        data = request.get_json()
        dni = data["dni"]
        password = data["password"]

        user = usecase_login(dni, password)

        session["dni"] = user.dni
        session["tipo"] = user.tipo  #Esto es lo que guarda el tipo en sesión

        # Respondemos con JSON al frontend (como hace login.html)
        return jsonify({
            "message": "Login correcto",
            "user": {
                "dni": user.dni,
                "name": user.name,
                "tipo": user.tipo
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 401


@app.route("/reserve.html")
def load_reserve():
    return render_template("/reserve.html")

@app.route("/prior_to_paying.html")
def load_prior_to_paying():
    return render_template("/prior_to_paying.html")

@app.route("/successful_reservation.html")
def load_successful_reservation():
    return render_template("/successful_reservation.html")

@app.route("/singin.html")
def load_singin():
    return render_template("/singin.html")

@app.route("/panelUsuario.html")
def load_panelUsuario():
    return render_template("/panelUsuario.html")


@app.route("/categorie.html")  #Lara estuvo aki
def categorias():
    return render_template("categorie.html")

@app.route("/register_machinery.html")
def register_machine():
    return render_template("register_machinery.html")

@app.route("/panelAdmin.html")
def panel_administrador():
    #if session.get("tipo") != "admin":
    #    return redirect("/login.html")
    return render_template("panelAdmin.html")


@app.route("/register_categorie.html")
def render_register_categorie():
    return render_template("register_categorie.html")



# ---- METODOS USUARIO ---- #

@app.route("/login", methods=["POST"])
def login():
    
    #request_value = request.get_json()
    
   # if not request_value:
    #    return jsonify({"error": "No se recibieron datos JSON"}), 400

    #dni = request_value.get("dni")
    #password = request_value.get("password")

    #if not dni or not password:
    #    return jsonify({"error": "DNI y contraseña son obligatorios"}), 400

    #try:
    #    user = Auth.usecase_login(dni=dni, password=password)
    #    login_user(user)
#
    #    return jsonify({
    #        "user": {
    #            "dni": user.dni,
     #           "name": user.name,
    #            "lastname": user.lastname,
    #            "email": user.email
     #       }
    #    }), 200
   # except Exception as e:
    #    return jsonify({"error": str(e)}), 401
    try:
        data = request.get_json()
        user = Auth.usecase_login(dni=data['dni'], password=data['password'])  #<<------------------------------------------------------------
        return jsonify({
            "user": {
                "dni": user.dni,
                "name": user.name,
                "lastname": user.lastname,
                "email": user.email
            }
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 401


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Sesión cerrada exitosamente"}), 200


@app.route("/signin", methods=["POST"])
def signin():
    try:
        dni = request.form["dni"]
        email= request.form["email"]
        name = request.form["name"]
        lastname = request.form["lastname"]
        phone = request.form["phone"]
        birthdate = request.form["birthdate"]
        terms_accepted = "terms" in request.form
        dni_photo = request.files["dni_photo"]
        #employee_number=request_value.get("employee_number"),
        RequestUser.usecase_request_user(dni, email, name, lastname, phone, birthdate, terms_accepted)

        if dni_photo:
            filename = secure_filename(f"{dni}_{lastname}.jpg")
            filepath = os.path.join(app.config['UPLOAD_FOLDER_USER'], filename)
            dni_photo.save(filepath)
            relative_path = f"{app.config['UPLOAD_FOLDER_USER']}/{filename}"
        else:
            relative_path = None
        flash("Solicitud pendiente de confirmación")
        return redirect (url_for("load_login"))
    except Exception as e:
        flash(str(e))
        return redirect(url_for("load_singin"))

@app.route("/user/update_user", methods=["PUT"])
@login_required
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
@login_required
def change_password():
    request_value = request.get_json()
    ChangePassword(
        dni = request_value.get("dni"),
        password_Act = request_value.get("passwordAct"),
        password_New_1 = request_value.get("password1"),
        password_New_2 = request_value.get("password2")
    )
    return "", 204

@app.route("/admin/add_employee", methods=["PUT"])
@login_required
def add_employee():
    request_value = request.get_json()
    AddEmployee.usecase_add_employee(
        name = request_value.get("name"),
        lastname = request_value.get("lastname"),
        dni = request_value.get("DNI"),
        email = request_value.get("email"),
        phone = request_value.get("phone"),
        dateBirth = request_value.get("dateBirth"),
        employeeN = request_value.get("employeeN")
    )
    
# ---- MAQUINAS ----

@app.route("/machine/add_machine", methods=["POST"]) # TESTEADO -> TRUE
#@login_required
def add_machine():
    try:
        form = request.form
        file = request.files.get("image")

        patent=form.get('patent')

        if file and file.filename != "":
            filename = secure_filename(patent + ".jpg")
            folder_path = os.path.join("static", "image", "machines")
            os.makedirs(folder_path, exist_ok=True)
            file.save(os.path.join(folder_path, filename))

        description = form.get("description")
        if description == None:
            description = ""

        AddMachine.usecase_add_machine(
            patent=patent,
            mark=form.get("mark"),
            model=form.get("model"),
            price_day=float(form.get("price_day")),
            ubication=form.get("ubication"),
            refund=float(form.get("refund")),
            categorie=form.get("categorie"),
            description=description
        )
        return "", 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/machine/enable_machine", methods=["POST"]) 
def enable_machine():
    try:
        request_value = request.get_json().get("patent")
        EnableMachine.usecase_enable_machine(patent=request_value)
        return "", 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/machine/disable_machine", methods=["POST"])
def disable_machine():
    try:
        request_value = request.get_json().get("patent")
        DisableMachine.usecase_disable_machine(patent=request_value)
        return "", 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/machine/get_all", methods=["GET"])  # TESTEADO -> TRUE
def get_all_machines():
    try:
        return jsonify( { "value" : GetAllMachines.usecase_get_all_machines()} ), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/machine/get_all_filter", methods=["GET", "POST"])  # TESTEADO -> TRUE
def get_all_machines_filter():
    # json del request = { "categorie": { "apply": True, "categorie": "Jardineria" }, "string": { "apply": False }, "price": { "apply": True, "price": 10.5 }}
    try:
        return jsonify(GetAllMachinesByFilter.usecase_get_all_machines_by( 
            categorie_filter=request.get_json().get("categoire"),
            string_filer=request.get_json().get("string"),
            price_filter=request.get_json().get("price"),
            mark_filter=request.get_json().get("mark"),
            model_filter=request.get_json().get("model"))), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ---- CATEGORIAS ----

@app.route("/categorie/add_categorie", methods=["POST"])  # TESTEADO -> TRUE
def add_categorie():
    try:
        request_value = request.get_json()
        AddCategorie.usecase_add_categorie(
            categorie=request_value.get("categorie")
        )
        return "", 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/categorie/enable_categorie", methods=["GET"])
def enable_categorie_get():
    try:
        return jsonify({ "categories": GetAllCategories.usecase_get_all_categories() })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/categorie/enable_categorie", methods=["POST"])
def enable_categorie_post():
    try:
        request_value = request.get_json().get("categorie")
        EnableCategorie.usecase_enable_categorie(categorie=request_value)
        return "", 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/categorie/disable_categorie", methods=["POST"])
def disable_categorie():
    try:
        request_value = request.get_json().get("categorie")
        DisableCategorie.usecase_disable_categorie(categorie=request_value)
        return "", 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ---- RESERVAS ----

@app.route("/reservation/machine_reservations", methods=["GET", "POST"]) # reservas de una maquina
def machine_reservations():
    try:
        request_value = request.get_json().get("machine_id")
        return jsonify({ "value" :  MachineReservations.usecase_get_all_reservations_by_machine(request_value) }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/reservation/reserve_machine", methods=["GET", "POST"]) # obtener reservas de una maquina
def reserve_machine():

    # fecha_hora = datetime.now()
    # fecha_hora = fecha_hora.strftime("%d/%m/%Y %H:%M:%S")
    # formate de las fechas

    # now = datetime.now()
    # date2 = now + timedelta(days=3)
    # date2_1 = now + timedelta(days=4)
    try:
        print()
        return "", 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ---- PAGOS ---- # COMENTADO A DREDE

@app.route("/pay/redirect_to_pay", methods=["GET", "POST"]) # Metodo iniciado por el boton de 'reservar'
def redirect_to_pay():
    try:
        #request_value = request.get_json()

        #preference = AddReservation.usecase_add_reserve(
            #start_day=request_value.get("start_day"),
            #end_day=request_value.get("end_day"),
            #client_id=request_value.get("client_id"),
            #machine_id=request_value.get("machine_id"),
            #shipment=request_value.get("shipment"),
        #)

        return jsonify({ "preference": PayByMercadoPago.execute() }), 200 
    except Exception as e:
        return jsonify({ "message": e }), 404

# RESPUESTAS DE PAGO

@app.route("/pay/successful_payment", methods=["GET"]) # Llamar al caso de uso que confirme la reserva
def successful_payment():
    try:

        return "", 204
    except Exception as e:
        return jsonify({ "message": e }), 404

# ---- MAIN ----

if __name__ == '__main__':
    app.run(debug=True)
    appDataBase.create_database()
