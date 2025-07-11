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
        patent="ABC2", 
        mark="CAT", 
        model="Cargadora", 
        price_day=3_000, 
        ubication="Calle 2 y avenida 25", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para cargar",
        creation_date="1985-5-1")
    
    AddMachine.usecase_add_machine(
        patent="ABC3", 
        mark="CAT", 
        model="Cargadora", 
        price_day=1_000, 
        ubication="Calle 3 y avenida 13", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para cargar",
        creation_date="2000-10-5")
    
    AddMachine.usecase_add_machine(
        patent="ABC1", 
        mark="CAT", 
        model="Excavadora", 
        price_day=3_000, 
        ubication="Calle 1 y avenida 12", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para excavar",
        creation_date="2000-10-5")
    
    # MAQUINA A DESHABILITAR
    AddMachine.usecase_add_machine(
        patent="ABC4", 
        mark="CAT", 
        model="Excavadora", 
        price_day=7_500, 
        ubication="Calle 4 y avenida 24", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para excavar",
        creation_date="2000-10-5")
    
    # MAQUINA A MOSTRAR BOTON CANCELAR GRIS
    AddMachine.usecase_add_machine(
        patent="ABC5", 
        mark="CAT", 
        model="Cargadora", 
        price_day=15_000, 
        ubication="Calle 5 y avenida 15", 
        refund=10, 
        categorie=["Construccion"], 
        description="Ideal para trasportar",
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
        password="45400389",
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
        email="josefina@gmail.com",
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
        start_day="2025-07-11", #--> 11
        end_day="2025-07-19",
        client_id=44555666, # ----> RESERVA DE nahuel
        machine_id="ABC1",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-08-22", 
        end_day="2025-08-30",
        client_id=44555666, # ----> RESERVA PARA MOSTRAR EL BLOQUEO DE DIAS
        machine_id="ABC2",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

    AddReservation.init_usecase_add_reserve(
        start_day="2025-08-15",
        end_day="2025-08-25",
        client_id=44555666, # ----> RESERVA DE Nahuel empleado
        machine_id="ABC3",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )


    # MAQUINA A DESHABILITAR
    AddReservation.init_usecase_add_reserve(
        start_day="2025-09-11",
        end_day="2025-09-25",
        client_id=45400389, 
        machine_id="ABC4",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )
    
    # MAQUINA A MOSTRAR BOTON CANCELAR GRIS
    AddReservation.init_usecase_add_reserve(
        start_day="2025-07-11",
        end_day="2025-07-25",
        client_id=45400389, 
        machine_id="ABC5",
        shipment=False,
        type="Cliente",
        apply_discount=False
    )

def __ALQUILERES__(): 
    AddRent.usercase_add_rent(
        start_day="2025-07-10",
        end_day="2025-07-18",
        client_id=45400389, # --> ALQUILER DE JUAN 
        machine_id="ABC2",      
        employee_id=4444        
    )
    
    # MAQUINA A DESHABILITAR
    AddRent.usercase_add_rent(
        start_day="2025-07-10",
        end_day="2025-07-18",
        client_id=45400389, # --> ALQUILER DE JUAN 
        machine_id="ABC4",      
        employee_id=4444        
    )












































