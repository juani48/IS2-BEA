from operator import and_
from data.config import session
from data.model.RentModel import RentModel

def execute(start_day, client_id, machine_id):
    rent = session.query(RentModel).filter(
        and_(
            and_(
                RentModel.start_day == start_day,
                RentModel.client_id == client_id
            ),
            RentModel.machine_id == machine_id
        )
    ).first()

    rent.canceled_by_maintenance = True
    session.commit()