from sqlalchemy import and_
from data.config import session
from data.model.ReservationModel import ReservationModel
from data.model.RentModel import RentModel

def execute(machine_id):
    list =  session.query(
        ReservationModel
    ).filter(
        and_(
            ReservationModel.machine_id == machine_id,
            ReservationModel.activate == False
        )
        
    ).all() #esta parte la tuve que cambiar porque estaba tirando errores
    return list




##
# 
# .join(
 ##       RentModel,
   
   #     and_(
    
    #        and_(
     #           ReservationModel.start_day == RentModel.start_day,
      #          ReservationModel.client_id == RentModel.client_id
       #     ),
        #    ReservationModel.machine_id == RentModel.machine_id
  #      )
   # )
# 
# ##