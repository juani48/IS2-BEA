from core.usecase.categorie import AddCategorie
from core.usecase.machine import AddMachine
from core.usecase.reserve import AddReservation
from core.usecase.rent import AddRent
from data.query.insert import query_insert_rent
from data.query.update import query_update_user_points
from data.query.insert import query_TEST_USER
from data.model.UserModel import UserModel
from data.appDataBase import create_database


def __init_db__():
    try:
        create_database()
        __CATEGORIAS__()
        __MAQUINAS__()
        __ADMIN__()
        __USUARIOS__()
        __EMPLEADOS__()
        __RESERVAS__()
        #__ALQUILERES__() #-> para testear el extender alquiler (pri)
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
        patent="ABC2", 
        mark="CAT", 
        model="Excavadora", 
        price_day=3_000, 
        ubication="Avenida 1 Calle 80", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para excavar",
        creation_date="1985-5-1")
    
    AddMachine.usecase_add_machine(
        patent="ABC3", 
        mark="CAT", 
        model="Cargadora", 
        price_day=1_000, 
        ubication="Ubicacion ABC3", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para cargar",
        creation_date="2000-10-5")
    
    AddMachine.usecase_add_machine(
        patent="C4R", 
        mark="CAT", 
        model="Cargadora", 
        price_day=3_000, 
        ubication="Ubicacion C4R", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para cargar",
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
            employee_number=1,
            type="Admin",
            authorized=True
        )
    query_TEST_USER.execute(user=admin)

def __USUARIOS__():
    
    juan = UserModel(
        dni=45400389,
        email="jibyrab@gmail.com",
        name="Juan",
        lastname="Brecevich",
        phone=123456788,
        birth_date="2004-6-28",
        password="juan",
        employee_number=0,
        type="Cliente",
        authorized=True)
    query_TEST_USER.execute(user=juan)
    query_update_user_points.execute(dni=45400389, number=5)

def __EMPLEADOS__():
    empleadoNahu = UserModel(
        dni=44555666,
        email="nahuHiriart@gmail.com",
        name="Nahuel",
        lastname="Hiriart",
        phone=25836914,
        birth_date="2003-11-5",
        password="44555666",
        employee_number=4444,
        type="Empleado",
        authorized=True)
    query_TEST_USER.execute(user=empleadoNahu)

    jose = UserModel(
        dni=66555444,
        email="jibyrab@gmail.com",
        name="Josefina",
        lastname="Pereyra",
        phone=123456788,
        birth_date="2004-6-28",
        password="66555444",
        employee_number=5555,
        type="Empleado",
        authorized=True)
    query_TEST_USER.execute(user=jose)

def __RESERVAS__():
    AddReservation.init_usecase_add_reserve(
        start_day="2025-7-12",
        end_day="2025-7-19",
        client_id=45400389, # ----> RESERVA DE Juan
        machine_id="ABC2",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-7-4",
        end_day="2025-7-13",
        client_id=44555666, # ----> RESERVA DE Nahuel empleado
        machine_id="C4R",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

def __ALQUILERES__(): #--> para testear el extender alquiler (pri)
    AddRent.usercase_add_rent(
        start_day="2025-7-2",
        end_day="2025-7-9",
        client_id=45400389,     
        machine_id="ABC2",      
        employee_id=None        
    )
    












































