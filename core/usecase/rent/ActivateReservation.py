from data.appDataBase import update_reservation_to_rent, get_employee

def usercase_activate_reservation(start_day, client_id, machine_id, employee_id):

    employee = get_employee(employee_id)

    print(client_id)
    print(type(client_id))
    print(employee.dni)
    print(employee.dni == client_id)
    if (int(client_id) == employee.dni):
        print("wtf")
        raise Exception("Alquiler fallido por coincidencia de DNI.")

    update_reservation_to_rent(start_day, client_id, machine_id, employee_id)