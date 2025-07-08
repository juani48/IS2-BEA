from core.usecase.categorie import AddCategorie
from core.usecase.machine import AddMachine
from core.usecase.reserve import AddReservation
from core.usecase.rent import AddRent
from data.query.insert import query_insert_rent
from data.query.update import query_update_user_points
from data.query.insert import query_TEST_USER
from data.model.UserModel import UserModel
from data.appDataBase import create_database

from datetime import datetime

def __init_db__():
    try:
        create_database()
        __CATEGORIAS__()
        __MAQUINAS__()
        __ADMIN__()
        __USUARIOS__()
        __EMPLEADOS__()
        __RESERVAS__()
        __ALQUILERES__() #-> para testear el extender alquiler (pri)
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
        mark="CAT", 
        model="cargadora", 
        price_day=100_000, 
        ubication="Avenida 1 Calle 80", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para cargar",
        creation_date="1985-5-1")

    AddMachine.usecase_add_machine(
        patent="ABC2", 
        mark="CAT", 
        model="Excavadora", 
        price_day=1_000, 
        ubication="Ubicacion ABC2", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para excavar",
        creation_date="2000-10-5")
        
 

        
    
def __ADMIN__():
    admin = UserModel(
            dni=11222333,
            email="bobelalquilador@gmail.com",
            name="Bob",
            lastname="ADMIN",
            phone=555555555,
            birth_date="1975-1-1",
            password="ADMIN",
            employee_number=-1,
            type="Admin",
            authorized=True
        )
    query_TEST_USER.execute(user=admin)

def __USUARIOS__():
    Juliana = UserModel(
        dni=49087890,
        email="ju@gmail.com",
        name="Juliana",
        lastname="Perez",
        phone=12345678,
        birth_date="2004-6-28",
        password="contraseña123",
        employee_number=0,
        type="Cliente",
        authorized=True)
    query_TEST_USER.execute(user=Juliana) 


    jose = UserModel(
        dni=47654123,
        email="josepereyra@gmail.com",
        name="Josefina",
        lastname="Pereyra",
        phone=123456788,
        birth_date="2004-6-28",
        password="josefinita1",
        employee_number=0,
        type="Cliente",
        authorized=True)
    query_TEST_USER.execute(user=jose)
    query_update_user_points.execute(dni=47654123, number=4)

def __EMPLEADOS__():
    empleadoGonzalo = UserModel(
        dni=88433627,
        email="empleado88433627@gmail.com",
        name="Gonzalo",
        lastname="lopez",
        phone=11111111,
        birth_date="2002-5-15",
        password="pepito123",
        employee_number=1234,
        type="Empleado",
        authorized=True)
    query_TEST_USER.execute(user=empleadoGonzalo)

    empleadoNahu = UserModel(
        dni=44555666,
        email="nahuHiriart@gmail.com",
        name="Nahuel",
        lastname="Hiriart",
        phone=25836914,
        birth_date="2003-11-5",
        password="empleado2",
        employee_number=4444,
        type="Empleado",
        authorized=True)
    query_TEST_USER.execute(user=empleadoNahu)

    empleadoLara = UserModel(
        dni=74156741,
        email="laradevincenti@hotmail.com",
        name="Lara",
        lastname="Devincenti",
        phone=25836914,
        birth_date="2002-5-1",
        password="larita",
        employee_number=8888,
        type="Empleado",
        authorized=True)
    query_TEST_USER.execute(user=empleadoLara)

def __RESERVAS__():


    AddReservation.init_usecase_add_reserve(
        start_day="2025-7-8",
        end_day="2025-7-19",
        client_id=47654123, # ----> RESERVA DE Jose
        machine_id="ABC2",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-10-12",
        end_day="2025-10-19",
        client_id=47654123, # ----> RESERVA DE Jose
        machine_id="ABC2",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )
    
    #AddReservation.init_usecase_add_reserve( --> para testear el confirmar reserva (pri)
    #   start_day="2025-6-23",
    #    end_day="2025-8-25",
    #    client_id=47654123, # ----> RESERVA DE Jose
    #    machine_id="ABC2",
    #    shipment=True,
    #    type="Cliente",
    #    apply_discount=False
    #)

def __ALQUILERES__(): #--> para testear el extender alquiler (pri)
    AddRent.usercase_add_rent(
        start_day="2025-7-2",
        end_day="2025-7-9",
        client_id=47654123,     
        machine_id="ABC2",      
        employee_id=None        
    )
    












































