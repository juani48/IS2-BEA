from core.usecase.categorie import AddCategorie
from core.usecase.machine import AddMachine
from core.usecase.reserve import AddReservation
from data.query.update import query_update_user_points
from data.query.insert import query_TEST_USER
from data.model.UserModel import UserModel
from data.appDataBase import create_database

from datetime import datetime

def __init_db__():
    try:
        create_database()
        __CATEGORIAS__()
        #__MAQUINAS__()
        __ADMIN__()
        __USUARIOS__()
        __EMPLEADOS__()
        #__RESERVAS__()
    except Exception as e:
        print(f"La base de datos ya esta cargada: {e}")

def add_points():
    query_update_user_points.execute(dni=11222333, number=100_000)

def __CATEGORIAS__():
    AddCategorie.usecase_add_categorie(categorie="Jardineria")
    AddCategorie.usecase_add_categorie(categorie="Construccion")
    AddCategorie.usecase_add_categorie(categorie="Mineria")
    AddCategorie.usecase_add_categorie(categorie="Transporte")

def __MAQUINAS__():
    AddMachine.usecase_add_machine(
        patent="ABC1", 
        mark="Marca ABC1", 
        model="Modelo ABC1", 
        price_day=10_500, 
        ubication="Ubicacion ABC1", 
        refund=10, 
        categorie="Jardineria", 
        description="Descripcion de la maquina ABC1")

    AddMachine.usecase_add_machine(
        patent="ABC2", 
        mark="Marca ABC2", 
        model="Modelo ABC2", 
        price_day=30_500, 
        ubication="Ubicacion ABC2", 
        refund=10, 
        categorie="Construccion", 
        description="Descripcion de la maquina ABC2")
        
    AddMachine.usecase_add_machine(
        patent="123A", 
        mark="Marca 123A", 
        model="Modelo 123A", 
        price_day=27_750, 
        ubication="Ubicacion 123A", 
        refund=15, 
        categorie="Jardineria", 
        description="Descripcion de la maquina 123A")
    
    AddMachine.usecase_add_machine(
        patent="C1AB", 
        mark="Marca C1AB", 
        model="Modelo C1AB", 
        price_day=13_500, 
        ubication="Ubicacion C1AB", 
        refund=5, 
        categorie="Mineria", 
        description="Descripcion de la maquina C1AB")

    AddMachine.usecase_add_machine(
        patent="N2CA", 
        mark="Marca N2CA", 
        model="Modelo N2CA", 
        price_day=40_500, 
        ubication="Ubicacion N2CA", 
        refund=5, 
        categorie="Construccion", 
        description="Descripcion de la maquina N2CA")
        
    AddMachine.usecase_add_machine(
        patent="75TW", 
        mark="Marca 75TW", 
        model="Modelo 75TW", 
        price_day=50_750, 
        ubication="Ubicacion 75TW", 
        refund=18, 
        categorie="Transporte", 
        description="Descripcion de la maquina 75TW")
    
def __ADMIN__():
    admin = UserModel(
            dni=11222333,
            email="bobelalquilador@gmail.com",
            name="ADMIN",
            lastname="ADMIN",
            phone=0000,
            birth_date="0001-1-1",
            password="ADMIN",
            employee_number=-1,
            type="Admin",
            authorized=True
        )
    query_TEST_USER.execute(user=admin)

def __USUARIOS__():
    carlos = UserModel(
        dni=44555666, # ----> Cambiar el DNI de Carlos a 66555444
        email="carlosmartinez@gmail.com",
        name="Carlos",
        lastname="Martinez",
        phone=0000,
        birth_date="0001-2-1",
        password="contraseña 123",
        employee_number=0,
        type="Cliente",
        authorized=True)
    query_TEST_USER.execute(user=carlos) 

    usuario_con_puntos = UserModel(
        dni=43907096,
        email="usuario_con_puntos@gmail.com",
        name="Usuario",
        lastname="Con Puntos",
        phone=0000,
        birth_date="0001-3-1",
        password="UsuarioConPuntos",
        employee_number=0,
        type="User",
        authorized=True)
    query_TEST_USER.execute(user=usuario_con_puntos)
    query_update_user_points.execute(dni=43907096, number=10)

    usuario_sin_puntos = UserModel(
        dni=45872513,
        email="usuario_sin_puntos@gmail.com",
        name="Usuario",
        lastname="Sin Puntos",
        phone=0000,
        birth_date="0001-4-1",
        password="usuarioSinPuntos",
        employee_number=0,
        type="User",
        authorized=True)
    query_TEST_USER.execute(user=usuario_sin_puntos)
    query_update_user_points.execute(dni=45872513, number=4)

    jose = UserModel(
        dni=47654123,
        email="josepereyra@gmail.com",
        name="Jose",
        lastname="Fina",
        phone=0000,
        birth_date="0001-5-1",
        password="JoseFina",
        employee_number=0,
        type="User",
        authorized=True)
    query_TEST_USER.execute(user=jose)

    juan = UserModel(
        dni=45400389,
        email="jibyrab@gmail.com",
        name="Ju",
        lastname="An",
        phone=0000,
        birth_date="0001-6-1",
        password="JuAn",
        employee_number=0,
        type="User",
        authorized=True)
    query_TEST_USER.execute(user=juan)

def __EMPLEADOS__():
    empleado1 = UserModel(
        dni=99888777,
        email="empleado99888777@gmail.com",
        name="Empleado",
        lastname="1",
        phone=0000,
        birth_date="0001-5-1",
        password="empleado1",
        employee_number=1234,
        type="Empleado",
        authorized=True)
    query_TEST_USER.execute(user=empleado1)

    empleado2 = UserModel(
        dni=44555667,
        email="empleado44555667@gmail.com",
        name="Empleado",
        lastname="2",
        phone=0000,
        birth_date="0001-6-1",
        password="empleado2",
        employee_number=4321,
        type="Empleado",
        authorized=True)
    query_TEST_USER.execute(user=empleado2)

def __RESERVAS__():
    AddReservation.init_usecase_add_reserve(
        start_day="2025-5-2",
        #start_day=datetime.datetime(2025, 5, 2, 0, 0, 0),
        end_day="2025-5-9",
        #end_day=datetime.datetime(2025, 5, 9, 0, 0, 0),
        client_id=44555666, # ----> RESERVA DE CARLOS
        machine_id="ABC1",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-6-2",
        #start_day=datetime.datetime(2025, 6, 2, 0, 0, 0),
        end_day="2025-6-9",
        #end_day=datetime.datetime(2025, 6, 9, 0, 0, 0),
        client_id=44555666, # ----> RESERVA DE CARLOS
        machine_id="ABC1",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-7-2",
        #start_day=datetime.datetime(2025, 7, 2, 0, 0, 0),
        end_day="2025-7-9",
        #end_day=datetime.datetime(2025, 7, 9, 0, 0, 0),
        client_id=44555666, # ----> RESERVA DE CARLOS
        machine_id="ABC1",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-6-2",
        #start_day=datetime.datetime(2025, 6, 2, 0, 0, 0),
        end_day="2025-6-9",
        #end_day=datetime.datetime(2025, 6, 9, 0, 0, 0),
        client_id=44555666, # ----> RESERVA DE CARLOS
        machine_id="ABC2",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-7-3",
        #start_day=datetime.datetime(2025, 7, 2, 0, 0, 0),
        end_day="2025-7-9",
        #end_day=datetime.datetime(2025, 7, 9, 0, 0, 0),
        client_id=44555666, # ----> RESERVA DE CARLOS
        machine_id="123A",
        shipment=True,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-6-2",
        #start_day=datetime.datetime(2025, 6, 2, 0, 0, 0),
        end_day="2025-6-9",
        #end_day=datetime.datetime(2025, 6, 9, 0, 0, 0),
        client_id=45400389, # ----> RESERVA DE JUAN
        machine_id="ABC2",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-7-2",
        #start_day=datetime.datetime(2025, 7, 2, 0, 0, 0),
        end_day="2025-7-9",
        #end_day=datetime.datetime(2025, 7, 9, 0, 0, 0),
        client_id=45400389, # ----> RESERVA DE JUAN
        machine_id="ABC2",
        shipment=True,
        type="Cliente",
        apply_discount=False
    )




















































