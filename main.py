from datetime import datetime, timedelta
import json
from flask import Flask, jsonify, render_template, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from core.entity.User import User
from data.appDataBase import get_user
from flask import redirect # redirigir a mercado pago
from core.service.mercado_pago import PayByMercadoPago
from core.service.mercado_pago.config import MP_SDK
from data import appDataBase
from core.usecase.user import Auth, UpdateUser,ChangePassword,RequestUser,AddEmployee,ReplyRequest
from core.usecase.machine import AddMachine, EnableMachine, DisableMachine, GetAllMachines, GetAllMachinesByFilter
from core.usecase.categorie import AddCategorie, EnableCategorie, DisableCategorie, GetAllCategories
from core.usecase.reserve import MachineReservations, AddReservation, ConfirmReservation, CancelReservation
from templates import *
import os
from werkzeug.utils import secure_filename
from flask import redirect, url_for
from flask import flash
from data.query.insert import query_TEST_USER
from data.model.UserModel import UserModel
from data.query.get.query_get_machine import execute
from data.config import session
from data.model.MachineCategorieModel import MachineCategorieModel
from data.model.CategorieModel import CategorieModel




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

import os
from werkzeug.utils import secure_filename

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
    #AddMachine.usecase_add_machine("A", "marcaA", "modeloA", 10, "ubicacionA", 10, "categoria1", "")
    #AddMachine.usecase_add_machine("B", "marcaB", "modeloB", 4, "ubicacionB", 30, "categoria1", "")
    #AddMachine.usecase_add_machine("C", "marcaC", "modeloC", 10, "ubicacionC", 15, "categoria2", "")

    #print(GetAllMachinesByFilter.usecase_get_all_machines_by(
        #categorie_filter={"apply": False, "categorie": "categoria1"}, 
        #string_filer={ "apply": True, "string": "lob" },
        #price_filter={ "apply": False, "price": 5 },
        #mark_filter={ "apply": False },           
        #model_filter={ "apply": False },
        #)
    #)
    
    # prueba de reservas
    # now = datetime.now(); date1 = now + timedelta(days=1); date1_1 = now + timedelta(days=2); date2 = now + timedelta(days=3); date2_1 = now + timedelta(days=4)
    
    #AddReservation.usecase_add_reserve(date1, date1_1, 1, "A1", 0, False)
    #AddReservation.usecase_add_reserve(date2, date2_1, 1, "A1", 0, False)
    #print({"value" : MachineReservations.usecase_get_all_reservations_by_machine("A1")})

    #query_TEST_USER.execute(22333444, user=UserModel(
        #dni=22333444, email="bb@gmail.com", name="ADMIN", lastname="JUAN", phone=22333444, birth_date="cumpleañitos", password=12345, type="Admin"
    #))

    return render_template('/main.html')

# ---- RENDERIZAR PAGINAS ---- #

@app.route('/main.html')
def load_home():
    return render_template('/main.html')

#@app.route('/machinery.html')
#def load_machinery():
#    return render_template('/machinery.html') 

@app.route('/machinery.html')
def load_machinery():
    machines = GetAllMachines.usecase_get_all_machines()  # obtiene todas las máquinas activas
    return render_template('machinery.html', machines=machines)


@app.route("/login.html")
def load_login():
    return render_template("login.html")



@app.route("/reserve.html")
@login_required
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
@login_required
def load_panelUsuario():
    return render_template("/panelUsuario.html")

@app.route("/panelAdmin.html")
@login_required
def load_panelAdministrador():
    if (current_user.type  == "Admin"):
        return render_template("/panelAdmin.html")
    else: 
        return render_template('/main.html')

@app.route("/categorie.html") 
def categorias():
    return render_template("categorie.html")

@app.route("/register_machinery.html")
@login_required
def register_machine():
    if (current_user.type  == "Admin"):
        return render_template("register_machinery.html")
    else:
        return "Solo los admin pueden cargar maquinarias"
    
@app.route("/register_categorie.html")
def register_categorie():
    return render_template("register_categorie.html")


@app.route('/description_machinery.html')
def description_machinery():
    return render_template('description_machinery.html')


# ---- METODOS USUARIO ---- #

def getType():                                   #Chequeado ✅
    return str(current_user.type)

@app.route("/login", methods=["POST"])           #Chequeado ✅
def login():
    try:
        data = request.get_json()
        userModel  = Auth.usecase_login(dni=data["dni"], password=data["password"])
        user = User(userModel)  # ✅ forma correcta
        login_user(user,remember= False)
        return jsonify({
            "user": {
                "dni": userModel.dni,
                "name": userModel.name,
                "lastname": userModel.lastname,
                "email": userModel.email,
                "type" : userModel.type
            }
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 401 


@app.route("/logout", methods=["POST"])          #Chequeado ✅
def logout():
    logout_user()
    return redirect(url_for('load_login'))


@app.route("/signin", methods=["POST"])          #Chequeado ✅
def signin():
    try:
        dni = request.form["dni"]
        email= request.form["email"]
        name = request.form["name"]
        lastname = request.form["lastname"]
        phone = request.form["phone"]
        birthdate = request.form["birthdate"]
        dni_photo = request.files["dni_photo"]
        RequestUser.usecase_request_user(dni, email, name, lastname, phone, birthdate)

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
    
@app.route("/session/status", methods=["GET"])
def session_status():
    if current_user.is_authenticated:
        return jsonify({
            "authenticated": True,
            "name": current_user.name,
            "type": current_user.type
        }), 200
    else:
        return jsonify({ "authenticated": False }), 200



@app.route("/user/update_user", methods=["PUT"]) #Chequeado ✅
@login_required
def update_user():         
    request_value = request.get_json()
    if (current_user.dni == request_value.dni):
        UpdateUser.usecase_update_user(
            #email=request_value.get("email"),
            dni = request_value.get("dni"),
            name =request_value.get("name"),
            lastname =request_value.get("lastname"),
        )
        return "", 204
    else:   
        return jsonify("DNI incoincidente"), 401


@app.route("/user/change_password", methods=["PUT"]) #Chequeado ✅ (falta aplicar hash)
@login_required
def change_password():
    request_value = request.get_json()
    if (current_user.dni == request_value.dni):
        ChangePassword(
            dni = request_value.get("dni"),
            password_Act = request_value.get("passwordAct"),
            password_New_1 = request_value.get("password1"),
            password_New_2 = request_value.get("password2")
        )
        return "", 204
    else: 
        return jsonify("DNI incoincidente"), 401


@app.route("/admin/add_employee", methods=["PUT"])   #Chequeado ✅
@login_required
def add_employee():
    request_value = request.get_json()
    if (current_user.type == "Admin"):
        AddEmployee.usecase_add_employee(
            name = request_value.get("name"),
            lastname = request_value.get("lastname"),
            dni = request_value.get("dni"),
            email = request_value.get("email"),
            phone = request_value.get("phone"),
            dateBirth = request_value.get("dateBirth"),
            employeeN = request_value.get("employeeN")
        )
    else:
        return "Debe ser administrador para agregar un empleado", 404
    return "Empleado agregado", 204

@app.route("/employee/requests", methods= ["PUT"])
@login_required
def reply_request():
    if current_user.type not in ["Admin", "Empleado"]:
        return jsonify({"error": "No tiene acceso aquí"}), 403
    try:
        request_value = request.get_json()
        reply = request_value.get("reply")
        dni = request_value.get("dni")
        if reply is None or dni is None:
            return jsonify({"error": "Faltan datos obligatorios (Reply o DNI)"}), 400
        RequestUser(reply=reply, dni=dni)
        return jsonify({"message": "Solicitud procesada correctamente"}), 200
    
    except Exception as e:
        return jsonify({"error": "Ocurrió un error al procesar la solicitud", "detalles": str(e)}), 500


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

@app.route("/machine/get_all", methods=["GET"])  # TESTEADO -> TRUE
def get_all_machines():
    return jsonify( { "value" : GetAllMachines.usecase_get_all_machines()} ), 200 

    
@app.route("/machine/get_all_filter", methods=["GET" , "POST"])
def get_all_machines_filter():
     # json del request = { "categorie": { "apply": True, "categorie": "Jardineria" }, "string": { "apply": False },
     #  "price": { "apply": True, "price": 10.5 }}

    try:
        data = request.get_json()

        return jsonify(GetAllMachinesByFilter.usecase_get_all_machines_by( 
            categorie_filter=data.get("categorie"),
            string_filer=data.get("string"),
            price_filter=data.get("price"),
            mark_filter=data.get("mark"),
            model_filter=data.get("model"))), 200

    except Exception as e:
        return jsonify({ "message": str(e) }), 404
    

@app.route("/machine/get_by_id/<string:machine_id>", methods=["GET"])
def get_machine_by_id(machine_id):
    machine = execute(machine_id)
    if not machine:
        return jsonify({"error": "Maquinaria no encontrada"}), 404

    # Obtener categorías asociadas
    categories = (
        session.query(CategorieModel.name)
        .join(MachineCategorieModel, MachineCategorieModel.categorie_id == CategorieModel.name)
        .filter(MachineCategorieModel.machine_id == machine_id)
        .all()
    )
    category_names = [cat.name for cat in categories]  # lista de strings

    machine_dict = machine.json()
    machine_dict["categories"] = category_names  #  sobrescribo "categorie" con lista

    return jsonify(machine_dict)



#    ---- CATEGORIAS ---- #

@app.route("/categorie/add_categorie", methods=["GET", "POST"])  # TESTEADO -> TRUE
def add_categorie():
    try:
        request_value = request.get_json()
        #print(request_value.get("categorie"))
        AddCategorie.usecase_add_categorie(
            categorie=request_value.get("categorie")
            
        )
        return "", 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/categorie/get_all_categories", methods=["GET"])
def get_all_categories():
    try:
        return jsonify({ "categories": GetAllCategories.usecase_get_all_categories()}) 
    except Exception as e:
        return jsonify({"error": str(e)}), 400 


@app.route("/categorie/enable_categorie", methods=["POST"])
def enable_categorie():
    request_value = request.get_json().get("categorie")
    EnableCategorie.usecase_enable_categorie(categorie=request_value)
    return "", 204

@app.route("/categorie/disable_categorie", methods=["GET", "POST"])
def disable_categorie():
    request_value = request.get_json().get("categorie")
    DisableCategorie.usecase_disable_categorie(categorie=request_value)
    return "", 204

# ---- RESERVAS ---- #

@app.route("/reservation/machine_reservations", methods=["GET", "POST"]) # reservas de una maquina
def machine_reservations():
    
    try:
        request_value = request.get_json().get("machine_id")
        return jsonify({ "value" :  MachineReservations.usecase_get_all_reservations_by_machine(request_value) }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/reservation/cancel_reservation", methods=["POST"])
def cancel_reservation():
    try:
        request_value = request.get_json()
        CancelReservation.usecase_cancel_reservation(
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            start_day=request_value.get("start_day")
        )
        return "", 204
    except Exception as e:
        return jsonify({ "message": e }), 404

@app.route("/reservation/reserve_machine", methods=["GET", "POST"]) # METODO ACTIVADO POR EL BOTON RESERVAR
def reserve_machine():
    try:
        request_value = request.get_json()

        preference = AddReservation.usecase_add_reserve(
            start_day=request_value.get("start_day"),
            end_day=request_value.get("end_day"),
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            shipment=request_value.get("shipment"),
        )

        return jsonify({ "preference": preference }), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ---- PAGOS ---- # 

#@app.route("/pay/redirect_to_pay", methods=["GET"]) # PROVISORIO
#def redirect_to_pay():
    try:
        request_value = request.get_json()

        AddReservation.usecase_add_reserve(
            start_day=request_value.get("start_day"),
            end_day=request_value.get("end_day"),
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            shipment=request_value.get("shipment"),
        )
        return "", 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/failure_reservation.html") # Llamar al caso de uso que CANCELE la reserva
def failure_reservation():
    preference_id = request.args.get('preference_id')
    print(preference_id)
    CancelReservation.usecase_cancel_reservation(preferences_id=preference_id)
    return render_template("failure_reservation.html")

@app.route("/pay/pay_notification", methods=["POST"]) # Verificar que se realizo el pago y enviar un correo
def pay_notification():
    try:
        request_value = request.get_json()
        topic = request_value.get("topic")
        
        if topic != None:
            ConfirmReservation.usecase_confirm_reservation(topic, request_value)
        return "", 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ---- MAIN ----

if __name__ == '__main__':
    app.run(debug=True)
    appDataBase.create_database()