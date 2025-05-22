from datetime import datetime, timedelta
import json
from flask import Flask, jsonify, render_template, request
from flask import redirect # redirigir a mercado pago
from core.service.mercado_pago import PayByMercadoPago
from data import appDataBase
from core.usecase.user import Login, Signin, UpdateUser,ChangePassword
from core.usecase.machine import AddMachine, EnableMachine, DisableMachine, GetAllMachines, GetAllMachinesByFilter
from core.usecase.categorie import AddCategorie, EnableCategorie, DisableCategorie
from core.usecase.reserve import MachineReservations, AddReservation
from templates import *

app = Flask(__name__)	

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

@app.route("/prior_to_paying.html")
def load_prior_to_paying():
    return render_template("/prior_to_paying.html")

@app.route("/successful_reservation.html")
def load_successful_reservation():
    return render_template("/successful_reservation.html")

# ---- METODOS USUARIO ---- #

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

# ---- MAQUINAS ----

@app.route("/machine/add_machine", methods=["GET", "POST"]) # TESTEADO -> TRUE
def add_machine():
    try:
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
    except Exception as e:
        return jsonify( { "message": e } ), 404

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
        return jsonify({ "message": e }), 404

# ---- CATEGORIAS ----

@app.route("/categorie/add_categorie", methods=["GET", "POST"])  # TESTEADO -> TRUE
def add_categorie():
    try:
        request_value = request.get_json()
        AddCategorie.usecase_add_categorie(
            categorie=request_value.get("categorie")
        )
        return "", 204
    except Exception as e:
        return jsonify({ "message": e }), 404

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

# ---- RESERVAS ----

@app.route("/reservation/machine_reservations", methods=["GET", "POST"]) # reservas de una maquina
def machine_reservations():
    
    try:
        request_value = request.get_json().get("machine_id")
        return jsonify({ "value" :  MachineReservations.usecase_get_all_reservations_by_machine(request_value) }), 200
    except Exception as e:
        return jsonify({ "message": e }), 404

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
        return "", 204
    except Exception as e:
        return jsonify({ "message": e }), 404


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
