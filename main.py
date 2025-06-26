import init_db_proyect
from datetime import datetime, timedelta
import json
from flask import Flask, jsonify, render_template, request,abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from core.entity.User import User
from data.appDataBase import get_machine, get_user
from flask import redirect # redirigir a mercado pago
from core.service.mercado_pago.config import MP_SDK
from core.usecase.user import Auth, UpdateUser,ChangePassword,RequestUser,AddEmployee,ReplyRequest, GetUserPoints, UpdateUserDni,GetAllRequests,DisableEmployee,RecoverPassword,GetAllEmployees, GetAllUsers, UserHistory, UserHistory,EnableEmployee
from core.usecase.machine import AddMachine, EnableMachine, DisableMachine, GetAllMachines, GetAllMachinesAdmin, GetAllMachinesByFilter, GetAllMachinesByFilterAdmin, UpdateMachine
from core.usecase.categorie import AddCategorie, EnableCategorie, DisableCategorie, GetAllCategories, GetAllCategoriesEnable
from core.usecase.reserve import MachineReservations, AddReservation, ConfirmReservation, CancelReservation, GetDailyReservations, GetAllReservations, UserReservations
from core.usecase.rent import AddRent, ActivateReservation, ExtendRent
from core.usecase.maintenance import StartMaintenance, EndMaintenance, GetAllMaintenance
from core.usecase.question import GetAllQuestions,AddQuestion
from core.usecase.commentary import GetAllCommentary,AddCommentary
from core.usecase.statistics import GetStatistics
from templates import *
import os
from werkzeug.utils import secure_filename
from flask import redirect, url_for
from flask import flash
from data.query.get.query_get_machine import execute
from data.config import session
from data.model.MachineCategorieModel import MachineCategorieModel
from data.model.CategorieModel import CategorieModel
from data.config import session
from data.model.ReservationModel import ReservationModel
from data.config import session
from data.model.ReservationModel import ReservationModel
from datetime import datetime
from core.usecase.machine import UpdateMachineUbication
from core.usecase.user.GetUserPoints import usecase_get_user_points
from data.query.get.query_get_discount import query_get_discount

from data.config import session





app = Flask(__name__)

app.secret_key = 'B3bQh7#2d@xZ!59sP0mT&vL'
UPLOAD_FOLDER_USER = 'static/image/users'
app.config['UPLOAD_FOLDER_USER'] = UPLOAD_FOLDER_USER
os.makedirs(UPLOAD_FOLDER_USER, exist_ok=True)	

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER_MACHINE = 'static/image/machines'
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
    return render_template('/main.html')

@app.route('/init_db_proyect')
def __init_db_proyect__():
    init_db_proyect.__init_db__()
    return load_home()

@app.route('/add_points')
def __add_points__():
    init_db_proyect.add_points()
    return load_home()

# ---- RENDERIZAR PAGINAS ---- #

@app.route('/main.html') #No hace falta estar logueado para entrar acá
def load_home():
    return render_template('/main.html')

@app.route('/machinery.html')
def load_machinery():
    if current_user.is_authenticated and current_user.type == "Admin":
        machines = GetAllMachinesAdmin.usecase_get_all_machines()  # incluye habilitadas y deshabilitadas
    else:
        machines = GetAllMachines.usecase_get_all_machines()  # solo habilitadas
    return render_template('machinery.html', machines=machines)


@app.route("/login.html") #No hace falta estar logueado para entrar acá
def load_login():
    return render_template("login.html")

@app.route("/forgot_password.html") #No hace falta estar logueado para entrar acá
def load_forgot_password():
    return render_template("forgot_password.html")


@app.route("/reserve.html") #Hace falta estar logueado para entrar acá
@login_required
def load_reserve():
    return render_template("/reserve.html")

@app.route("/prior_to_paying.html") #Hace falta estar logueado para entrar acá
@login_required
def load_prior_to_paying():
    return render_template("/prior_to_paying.html")

@app.route("/successful_reservation.html") #Hace falta estar logueado para entrar acá
@login_required
def load_successful_reservation():
    return render_template("/successful_reservation.html")

@app.route("/singin.html") #No hace falta estar logueado para entrar acá
def load_singin():
    return render_template("/singin.html")

@app.route("/panelUsuario.html") #Hace falta estar logueado para entrar acá, y tenés que ser cliente para verlo, 
@login_required                  # Si no sos usuario te manda al main (para visitantes)
def load_panelUsuario():
    if(current_user.type == "Cliente"):
        return render_template("/panelUsuario.html")
    else:
        return render_template("/main.html")

@app.route("/panelAdmin.html") #Hace falta estar logueado para entrar acá, y tenés que ser admin para verlo,
@login_required                # Si no sos admin te manda al main (para visitantes)
def load_panelAdministrador():
    if (current_user.type  == "Admin"):
        return render_template("/panelAdmin.html")
    else: 
        return render_template('/main.html')

@app.route("/panelEmpleado.html") #Hace falta estar logueado para entrar acá, y tenés que ser empelado para verlo,
@login_required                   #Si no sos empleado te manda al main (para visitantes)
def load_panelEmpleado():
    if(current_user.type == "Empleado"): 
        return render_template("/panelEmpleado.html")
    else:
        return render_template("/main.html")

@app.route("/statistics.html")
@login_required
def load_statistics():
    if(current_user.type == "Admin"):
        return render_template("/statistics.html")
    else:
        return render_template("/main.html")

@app.route("/change_password.html") #Hace falta estar logueado para entrar acá, no importa que tipo de usuario sos
@login_required
def load_change_password():
    return render_template("/change_password.html")

@app.route("/edit_profile.html") #Hace falta estar logueado para entrar acá, no importa que tipo de usuario sos
@login_required
def load_edit_profile():
    return render_template("/edit_profile.html")

@app.route("/edit_personal_data.html") #Hace falta estar logueado para entrar acá, no importa que tipo de usuario sos
@login_required
def load_edit_personal_data():
    return render_template("/edit_personal_data.html")

@app.route("/register_machinery.html") #Hace falta estar logueado para entrar acá y tenés que ser admin para entrar
@login_required                        #Si no sos admin te lleva al main
def register_machine():
    if (current_user.type  == "Admin"):
        return render_template("register_machinery.html")
    else:
        return render_template("/main")
    
@app.route("/register_categorie.html") #Hace falta estar logueado para entrar acá y tenés que ser admin o empleado (?)
@login_required                        #Si no sos admin o empleado te lleva al main
def register_categorie():              # chequear si los empleados tambien pueden cargar categorías
    if current_user.type in ["Admin", "Empleado"]:
        return render_template("register_categorie.html")
    else:
        return render_template("/main.html")
    
@app.route("/register_employee.html") #Hace falta estar logueado para entrar acá y tenés que ser admin para entrar
@login_required                       #Si no sos admin te lleva al main
def register_employee():
    if (current_user.type  == "Admin"):
        return render_template("register_employee.html")
    else:
        return render_template("/main")
    
@app.route("/pending_requests.html") #Hace falta estar logueado para entrar acá y tenes que ser empleado o admin
@login_required                      #Si no sos admin o empleado, te manda al main
def load_pending_request():
    if current_user.type in ["Admin", "Empleado"]:
        return render_template("pending_requests.html")
    else:
        return render_template("/main.html")
    
@app.route('/description_machinery.html') #No hace falta estar logueado para entrar aca
def description_machinery():
    return render_template('description_machinery.html')

@app.route("/list_reservation.html") #Hace falta estar logueado y ser empleado o admin
@login_required                      #Si no sos admin o empleado, te manda al main
def load_list_reservation():
    if current_user.type in ["Admin", "Empleado"]:
        return render_template("list_reservation.html")
    else:
        return render_template("/main.html")

@app.route('/list_employee.html') #Hace falta estar logueado y ser empleado o admin
@login_required                   #Si no sos admin o empleado, te manda al main
def list_employee():
    if current_user.type in ["Admin", "Empleado"]:
        return render_template('list_employee.html')
    else:
        return render_template("/main.html")

@app.route("/terminos.html")
def load_terminos():
    return render_template("terminos.html")

@app.route("/list_all_reservation.html")
@login_required                     
def load_all_reservation():
    if current_user.type in ["Admin", "Empleado"]:
        return render_template("list_all_reservation.html")
    else:
        return render_template("/main.html")
    
@app.route("/list_all_users.html")
@login_required
def load_list_clients():
    if current_user.type == "Admin":
        return render_template("list_all_users.html")
    return redirect("/main.html")

@app.route("/user_history.html")
@login_required
def user_history_page():
    return render_template("user_history.html")


@app.route('/list_categories.html') #Hace falta estar logueado y ser empleado o admin
@login_required                   #Si no sos admin o empleado, te manda al main
def list_categories():
    if current_user.type in ["Admin", "Empleado"]:
        return render_template('list_categories.html')
    else:
        return render_template("/main.html")
    

@app.route('/edit_machine_data.html') 
@login_required                   
def edit_machine_data():
    if current_user.type in ["Admin"]:
        return render_template('edit_machine_data.html')
    else:
        return render_template("/main.html")
    
@app.route("/rent_machine.html")
@login_required                     
def rent_machine_route():
    if current_user.type in ["Admin", "Empleado"]:
        return render_template("rent_machine.html")
    else:
        return render_template("/main.html")

    
# ---- METODOS USUARIO ---- #

def getType():                                   
    return str(current_user.type)

@app.route("/login", methods=["POST"])           
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


@app.route("/logout", methods=["POST"])          
def logout():
    try:
        logout_user()
        return redirect(url_for('load_login'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for("load_singin"))


@app.route("/signin", methods=["POST"])          
def signin():
    try:
        dni = request.form["dni"]
        email = request.form["email"]
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

        flash("Solicitud pendiente de confirmación", "success")
        return render_template("/login.html", registro_exitoso=True)

    except Exception as e:
        flash(str(e), "error")
        return render_template("/singin.html")

    
@app.route("/session/status", methods=["GET"])
def session_status():
    if current_user.is_authenticated:
        return jsonify({
            "dni": current_user.dni,
            "authenticated": True,
            "name": current_user.name,
            "lastname": current_user.lastname,
            "type": current_user.type
        }), 200
    else:
        return jsonify({ "authenticated": False }), 200

@app.route("/session/employee", methods=["GET"])
@login_required
def get_employee_session_info():
    if current_user.type == "Empleado" and current_user.employee_number > 0:
        return jsonify({ "employee_id": current_user.employee_number }), 200
    return jsonify({ "error": "No autorizado" }), 403



@app.route("/session/employee", methods=["GET"])
@login_required
def get_employee_number():
    if current_user.type == "Empleado" and current_user.employee_number > 0:
        return jsonify({ "employee_id": current_user.employee_number }), 200
    return jsonify({ "error": "No autorizado" }), 403

@app.route("/user/personal_data", methods=["GET", "PUT"])
@login_required
def personal_data():
    user = current_user

    if request.method == "GET":
        return jsonify({
            "name": user.name,
            "lastname": user.lastname,
            "dni": user.dni,
            "email": user.email,
            "phone": user.phone,
            "birthdate": user.birth_date,
            "points": user.points
        })

    # PUT
    data = request.get_json()
    UpdateUser.usecase_update_user(
        dni=user.dni,
        name=data["name"],
        lastname=data["lastname"],
        phone=data["phone"]
    )
    return "", 204


@app.route("/user/change_password", methods=["PUT"])
@login_required
def change_password():
    request_value = request.get_json()
    if current_user.dni == request_value.get("dni"):
        try:
            ChangePassword.usecase_change_password(
                dni=request_value.get("dni"),
                password_Act=request_value.get("passwordAct"),
                password_New_1=request_value.get("password1"),
                password_New_2=request_value.get("password2")
            )
            return "", 204
        except Exception as e:
            return jsonify({ "error": str(e) }), 400  # ✅ Mejora acá
    else:
        return jsonify({ "error": "DNI incoincidente" }), 401

@app.route("/user/recover_password", methods=["PUT"])
def recover_password():
    data = request.get_json()
    email = data.get("email")  # <- EXTRAÉS SOLO EL STRING
    RecoverPassword.usecase_recover_password(email)
    return "", 204  # <-- devolvé un 204 o lo que prefieras



@app.route("/admin/add_employee", methods=["PUT"])
@login_required
def add_employee():
    request_value = request.get_json()
    if current_user.type != "Admin":
        return "Debe ser administrador para agregar un empleado", 403

    try:
        AddEmployee.usecase_add_employee(
            name = request_value.get("name"),
            lastname = request_value.get("lastname"),
            dni = request_value.get("dni"),
            email = request_value.get("email"),
            phone = request_value.get("phone"),
            dateBirth = request_value.get("dateBirth"),
            employeeN = request_value.get("employeeN")
        )
        return "Empleado agregado", 204
    except Exception as e:
        return jsonify({"detalles": str(e)}), 500


@app.route("/employee/disable", methods=["POST"])
@login_required
def disable_employee():
    if(current_user.type == "Admin"):
        try:
            data = request.get_json()
            dni = data.get("dni")
            DisableEmployee.usecase_disable_employee(dni)
            return "", 204
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else: 
        return render_template("/main.html")




@app.route("/user/enable_employee", methods=["POST"])
@login_required
def enable_employee():
    try:
        data = request.get_json()
        dni = data.get("dni")
        nro = data.get("employee_number", 0)
        EnableEmployee.usecase_enable_employee(nro, dni)
        return "", 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@app.route("/employee/get_all", methods=["GET"])  
def get_all_employees():
    return jsonify( { "value" : GetAllEmployees.usecase_get_all_employees()} ), 200 

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
        ReplyRequest(reply=reply, dni=dni)
        return jsonify({"message": "Solicitud procesada correctamente"}), 200
    
    except Exception as e:
        return jsonify({"error": "Ocurrió un error al procesar la solicitud", "detalles": str(e)}), 500

@app.route("/requests/get_all", methods=["GET"])  
@login_required
def get_all_requests():
    if current_user.type in ["Admin", "Empleado"]:
        return jsonify( { "value" : GetAllRequests.usecase_get_all_requests()} ), 200 
    else:
        return render_template("/main.html")

@app.route("/user/update_user_dni", methods= ["POST"])
@login_required
def update_user_dni():
    if(current_user.type =="Admin"):
        try:
            request_value = request.get_json()
            UpdateUserDni.usecase_update_user_dni(
                dni=request_value.get("dni"),
                new_dni=request_value.get("new_dni")
            )
            return "", 204
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return render_template ("/main.html")


@app.route("/requests/reply", methods=["POST"])
@login_required
def reply_user_request():
    if(current_user.type in ["Empleado", "Admin"]):
        data = request.get_json()
        reply = data.get("reply")
        dni = data.get("dni")

        try:
            mensaje = ReplyRequest.usecase_reply_request(reply, dni)
            return jsonify({"mensaje": mensaje}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return render_template ("/main.html")

@app.route("/users/get_all_users")
@login_required
def get_all_clients():
    return jsonify(GetAllUsers.usecase_get_all_users()), 200


@app.route("/user/user_history", methods=["GET", "POST"])
def user_history():
    try:
        resultado = UserHistory.usecase_user_history(current_user.dni)
        return jsonify({ "value": [r.json() for r in resultado] })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/user/get_discount", methods=["GET"])
@login_required
def get_discount():
    try:
        dni = request.args.get("dni")
        if not dni:
            return jsonify({"error": "DNI no proporcionado"}), 400
        current_points = usecase_get_user_points(dni)  #  esto está bien
        discount = query_get_discount()
        discount = query_get_discount()
        if not discount:
            return jsonify({"error": "No hay política de descuento activa"}), 404

        if discount.need is None:
            return jsonify({"error": "El descuento de puntos no está bien configurado"}), 500

        if current_points >= discount.need:
            return jsonify({
                "can_use_discount": True,
                "percentage": discount.discount
            }), 200
        else:
            return jsonify({
                "can_use_discount": False,
                "percentage": discount.discount
            }), 200

    except Exception as e:
       return jsonify({"error": str(e)}), 500
    
@app.route("/user/user_points", methods=["GET","POST"])
def user_points():
    try: 
        request_value = request.get_json() # { "id": 12345 }
        return jsonify( GetUserPoints.usecase_get_user_points(request_value.get("dni")) ), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/question/get_all", methods=["GET"])
def get_all_questions():
    return jsonify( { "value" : GetAllQuestions.usecase_get_all_questions()} ), 200     

@app.route("/question/add_question", methods=["POST"])
@login_required
def add_question():
    try:
        data = request.get_json()
        if not data or not data.get("question"):     # Validaciones básicas
            return jsonify({"error": "La pregunta es obligatoria"}), 400
        
        user_dni = current_user.dni                # nombre del usuario logueado
        question_text = data["question"]

        AddQuestion.usecase_add_question(user_dni, question_text)
        return jsonify({"message": "Pregunta enviada correctamente"}), 201
    except Exception as e:
        return jsonify({"error": f"Error al agregar pregunta: {str(e)}"}), 500

@app.route("/commentary/get_all", methods=["POST"])
def get_all_commentary():
    data = request.get_json()
    machine_patent = data.get("machine_patent")
    return jsonify({ "value": GetAllCommentary.usecase_get_all_commentarys(machine_patent) }), 200

@app.route("/commentary/add_commentary", methods=["POST"])
@login_required
def add_commentary():
    try:
        data = request.get_json()
        if not data or not data.get("commentary"):     # Validaciones básicas
            return jsonify({"error": "El comentario es obligatorio"}), 400
        
        user_dni = current_user.dni                # dni del usuario logueado
        commentary_text = data["commentary"]
        patent = data ["patent"] 
        AddCommentary.usecase_add_commentary( machine_patent=patent, commentaryStr=commentary_text, dni=user_dni,)
        return jsonify({"message": "Comentario enviado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": f"Error al agregar comentario: {str(e)}"}), 500
    
# ---- MAQUINAS ----

@app.route("/machine/add_machine", methods=["POST"]) # TESTEADO -> TRUE
@login_required
def add_machine():
    if(current_user.type == "Admin"):
        try:
            form = request.form
            imagenes = request.files.getlist("images")

            patent=form.get('patent')

                        
            folder_path = os.path.join("static", "image", "machines")
            os.makedirs(folder_path, exist_ok=True)

            lista_nombres = []

            for i, img in enumerate(imagenes):
                if img and img.filename != "":
                    extension = os.path.splitext(img.filename)[1] or ".jpg"
                    nombre = f"{patent}({i+1}){extension}"
                    img.save(os.path.join(folder_path, nombre))
                    lista_nombres.append(nombre)

            # Guardar JSON con los nombres
            with open(os.path.join(folder_path, f"{patent}.json"), "w") as f:
                json.dump(lista_nombres, f)



            description = form.get("description")
            if description == None:
                description = ""
            
            categorie = form.getlist("categorie")

            AddMachine.usecase_add_machine(
                patent=patent,
                mark=form.get("mark"),
                model=form.get("model"),
                price_day=float(form.get("price_day")),
                ubication=form.get("ubication"),
                refund=float(form.get("refund")),
                categorie=categorie, # TIENE QUE SER UN ARREGLO AUNQUE SEA UNA CATEGORIA = { "cagorie": [ "PEPITO" ] }
                description=description,
                creation_date=form.get("creation_date")
            )
            return "", 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return render_template("/main.html")
    
@app.route("/machine/update_machine", methods=["POST"])
@login_required
def update_machine():
    if(current_user.type == "Admin"):
        try:
            request_value = request.get_json()
            UpdateMachine.usecase_update_machine(
                patent=request_value.get("patent"),
                mark=request_value.get("mark"),
                model=request_value.get("model"),
                price_day=request_value.get("price_day"),
                ubication=request_value.get("ubication") if "ubication" in request_value else None,
                refund=request_value.get("refund"),
                description=request_value.get("description"),
                creation_date=request_value.get("creation_date"),
                categorie=request_value.get("categorie")  #  esto es lo nuevo
            )
            return "", 204
        except Exception as e:
            return jsonify({ "message": str(e) }), 404
    else:
        return render_template("/main.html")

@app.route("/machine/update_ubication", methods=["POST"])
@login_required
def update_machine_ubication():
    if current_user.type == "Admin" or current_user.type == "Empleado":

        try:
            data = request.get_json()
            patent = data.get("patent")
            new_ubication = data.get("ubication")

            UpdateMachineUbication.usecase_update_machine_ubication(patent, new_ubication)

            return "", 204
        except Exception as e:
            return jsonify({"message": str(e)}), 500
    else:
        return jsonify({"message": "No autorizado"}), 403



@app.route("/machine/enable_machine", methods=["GET", "POST"]) 
@login_required
def enable_machine():
    if(current_user.type == "Admin"):
        try:
            request_value = request.get_json().get("patent")
            EnableMachine.usecase_enable_machine(patent=request_value)
            return "", 204
        except Exception as e:
            return jsonify({ "message": e }), 404
    else:
        return render_template ("/main.html")

@app.route("/machine/disable_machine", methods=["GET", "POST"])
@login_required
def disable_machine():
    if(current_user.type == "Admin"):
        try:
            request_value = request.get_json().get("patent")
            DisableMachine.usecase_disable_machine(patent=request_value)
            return "", 204
        except Exception as e:
            return jsonify({ "message": e }), 404
    else:
        return render_template("/main.html")

@app.route("/machine/get_all_machines", methods=["GET"])
def get_all_machines_main():
    try:
        return jsonify({"machines": GetAllMachines.usecase_get_all_machines()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@app.route("/machine/get_all_machines_admin", methods=["GET"])
def get_all_machines_main_admin():
    try:
        return jsonify({"machines": GetAllMachinesAdmin.usecase_get_all_machines()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    
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
    
@app.route("/machine/get_all_filter_admin", methods=["GET" , "POST"])
def get_all_machines_filter_admin():
     # json del request = { "categorie": { "apply": True, "categorie": "Jardineria" }, "string": { "apply": False },
     #  "price": { "apply": True, "price": 10.5 }}

    try:
        data = request.get_json()

        print(GetAllMachinesByFilterAdmin.usecase_get_all_machines_by_admin( 
            categorie_filter=data.get("categorie"),
            string_filer=data.get("string"),
            price_filter=data.get("price"),
            mark_filter=data.get("mark"),
            model_filter=data.get("model")))
        return jsonify(GetAllMachinesByFilterAdmin.usecase_get_all_machines_by_admin( 
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
    category_names = [cat[0] for cat in categories]  #  correcto, porque se retorna una tupla

    machine_dict = machine.json()
    machine_dict["categories"] = category_names  #  sobrescribo "categorie" con lista

    return jsonify(machine_dict)

@app.route("/machine/top3", methods=["GET"])
def get_top3_machines():
    all = GetAllMachines.usecase_get_all_machines()
    all = all[:3]
    return jsonify({ "machines": all }), 200


#    ---- CATEGORIAS ---- #

@app.route("/categorie/add_categorie", methods=["GET", "POST"])  # TESTEADO -> TRUE{}
@login_required
def add_categorie():
    if(current_user.type in ["Admin", "Empleado"]):
        try:
            request_value = request.get_json()
            #print(request_value.get("categorie"))
            AddCategorie.usecase_add_categorie(
                categorie=request_value.get("categorie")
            
            )
            return "", 204
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return render_template("/main.html")

@app.route("/categorie/get_all_categories", methods=["GET"])
def get_all_categories():
    try:
        return jsonify({ "categories": GetAllCategories.usecase_get_all_categories()}) 
    except Exception as e:
        return jsonify({"error": str(e)}), 400 

# este es para habilitar una categoria (para u  admin/empleado) --> si decis que es para empleado te creo entonces
@app.route("/categorie/enable_categorie", methods=["POST"])
@login_required
def enable_categorie():
    if(current_user.type =="Admin"):
        request_value = request.get_json().get("categorie")
        EnableCategorie.usecase_enable_categorie(categorie=request_value)
        return "", 204
    else:
        return render_template("/main.html")

@app.route("/categorie/disable_categorie", methods=["GET", "POST"])
@login_required
def disable_categorie():
    if(current_user.type in ["Empleado", "Admin"]):
        request_value = request.get_json().get("categorie")
        try:
            DisableCategorie.usecase_disable_categorie(categorie=request_value)
            return jsonify({"message": "Categoría deshabilitada"}), 200
        except Exception as e:
            return jsonify({"message": str(e)}), 400  #  importante: enviar el mensaje de error

    else:
        return ("/main.html")

# este es para hacer la lista de categorias disponibles
@app.route("/categories/enabled", methods=["GET"])
def get_enabled_categories():
    return jsonify(GetAllCategoriesEnable.usecase_get_all_categories())


# ---- RESERVAS ---- #

@app.route("/reservation/machine_reservations", methods=["GET", "POST"]) # reservas de una maquina
@login_required
def machine_reservations():
    
    try:
        request_value = request.get_json().get("machine_id") # [ star:.... , endfa....  ]
        return jsonify({ "value" :  MachineReservations.usecase_get_all_reservations_by_machine(request_value) }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
 
@app.route("/reservation/cancel_reservation", methods=["POST"])
@login_required
def cancel_reservation():
    try:
        request_value = request.get_json()
        CancelReservation.usecase_cancel_reservation_by_employee(
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            start_day=request_value.get("start_day")
        )
        return "", 204
    except Exception as e:
        return jsonify({ "message": str(e) }), 400

@app.route("/reservation/cancel_by_client", methods=["POST"])
@login_required
def cancel_reservation_by_client():
    try:
        data = request.get_json()
        # Opcional: validar que la reserva sea suya con current_user.id
        CancelReservation.usecase_cancel_reservation_by_client(
            preference_id=data.get("preference_id")
        )
        return "", 204
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/reservation/reserve_machine", methods=["GET", "POST"]) # METODO ACTIVADO POR EL BOTON RESERVAR
@login_required
def reserve_machine():
    try:
        request_value = request.get_json()
        #print("🔎 Datos recibidos:", request_value)  # ✅ AGREGADO
        preference = AddReservation.usecase_add_reserve(
            start_day=request_value.get("start_day"),
            end_day=request_value.get("end_day"),
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            shipment=request_value.get("shipment"),
            type=request_value.get("type"), # TIPO DE USUARIO - STRING
            apply_discount=request_value.get("apply_discount") # DESCUENTO - BOOLEANO
        )

        return jsonify({ "preference": preference }), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/reservation/get_daily_reservations", methods=["POST"])
def get_daily_reserve():
    try:
        return jsonify( GetDailyReservations.usecase_get_daily_reservations() ), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@app.route("/reservation/get_all_reservation", methods=["POST"])
def get_all_reservation():
    try:
        return jsonify(GetAllReservations.usecase_get_all_reservations()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
# ---- PAGOS ---- # 

@app.route("/failure_reservation.html") # Llamar al caso de uso que CANCELE la reserva
def failure_reservation():
    preference_id = request.args.get('preference_id')
    CancelReservation.usecase_cancel_reservation_by_client(preference_id=preference_id)
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

# ---- ALQUILERES ---- #

# ACTIVAR RESERVA PASANDOLA A ALQUILER
@app.route("/reservation/activate_reservation", methods=["POST"])
def activate_reservation():
    try:
        request_value = request.get_json()
        ActivateReservation.usercase_activate_reservation(
            start_day=request_value.get("start_day"),
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            employee_id=request_value.get("employee_id")
        )
        return "", 201
    except Exception as e:
        return jsonify({ "error": str(e) }), 404


# CARGAR ALQUILER (SE REALIZA EL MISMO DIA)
@app.route("/rent/rent_machine", methods=["POST"])
def rent_machine():
    try:
        request_value = request.get_json()
        AddRent.usercase_add_rent(
            start_day=request_value.get("start_day"),
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            end_day=request_value.get("end_day"),
            employee_id=request_value.get("employee_id")
        )
        return "", 201
    except Exception as e:
        return jsonify({ "error": str(e) }), 404

@app.route("/rent/extend_rent", methods=["POST"])
def extend_rent():
    print("📩 Llamada a /rent/extend_rent recibida")
    try:
        request_value = request.get_json()
        ExtendRent.usecase_extend_rent(
            start_day=request_value.get("start_day"),
            client_id=request_value.get("client_id"),
            machine_id=request_value.get("machine_id"),
            days_extended=request_value.get("days_extended")
        )
        return "", 201
    except Exception as e:
        return jsonify({ "error": str(e) }), 404

# ---- MANTENIMIENTOS ---- #
@app.route("/maintenance/start_maintenance", methods=["POST"])
def start_maintenance():
    try:
        request_value = request.get_json()
        StartMaintenance.usercase_start_maintenance(
            start_day=request_value.get("start_day"),
            client_id=request_value.get("client_id"),
            start_employee_id=request_value.get("start_employee_id"),
            machine_id=request_value.get("machine_id")
        )
        return "", 201
    except Exception as e:
        return jsonify({ "error": str(e) }), 404

@app.route("/maintenance/end_maintenance", methods=["POST"])
def end_maintenance():
    try:
        request_value = request.get_json()
        EndMaintenance.usercase_end_maintenance(
            start_day=request_value.get("start_day"),
            client_id=request_value.get("client_id"),
            start_employee_id=request_value.get("start_employee_id"),
            machine_id=request_value.get("machine_id"),
            end_employee_id=request_value.get("end_employee_id"),
            description=request_value.get("description")
        )
        return "", 201
    except Exception as e:
        return jsonify({ "error": str(e) }), 404

@app.route("/maintenance/get_all_maintenance", methods=["GET"])
def get_all_maintenance():
    try:
        return jsonify({ "maintenance": GetAllMaintenance.usecase_get_all_maintenance() })
    except Exception as e:
        return jsonify({ "error": str(e) }), 404


# ---- ESTADISTICAS ---- #

@app.route("/statistics/get_statistics", methods=["POST"])
def get_statistics():
    try:
        request_value = request.get_json()
        return jsonify({
            "statistics": GetStatistics.usecase_get_statistics(
                start_date=request_value.get("start_date"),
                end_date=request_value.get("end_date"),
                categorie=request_value.get("categorie")
            ) 
        })
    except Exception as e:
        return jsonify({ "error": str(e) }), 4


# ---- MAIN ----

if __name__ == '__main__':
    app.run(debug=True)
