from operator import and_
from data.config import session
from data.model.RentModel import RentModel
from data.model.ReservationModel import ReservationModel

def execute(start_day, client_id, machine_id, employee_id):
    local_reservation = session.query(
        ReservationModel
    ).filter(
        and_(
            ReservationModel.client_id == client_id,
            ReservationModel.machine_id == machine_id,
            ReservationModel.start_day == start_day
        )
    ).first()
    if(local_reservation == None):
        raise Exception("No existe una reserva para la maquina.")
    
    rent = RentModel(
        start_day=start_day,
        end_day=local_reservation.end_day,
        client_id=client_id,
        machine_id=machine_id,
        total_value=local_reservation.total_value,
        employee_id=employee_id
    )

    session.add(rent)
    local_reservation.activate = True
    local_reservation.employee_id = rent.employee_id
    session.commit()