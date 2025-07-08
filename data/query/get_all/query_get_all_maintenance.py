from data.config import session
from data.model.MaintenanceModel import MaintenanceModel

#def execute():
#    return session.query(MaintenanceModel).filter(MaintenanceModel.completed == False).all()

def execute():
    return session.query(MaintenanceModel).all()
