from data.config import session
from data.model.UserModel import UserModel

def execute(employeeN):
    if not employeeN:
        raise ValueError("El número de empleado no puede ser nulo o vacío")

    try:
        employee = session.query(UserModel).filter_by(employee_number=employeeN).first()
        return employee
    except Exception as e:
        raise RuntimeError(f"Error al obtener usuario por numero de empleado: {e}")