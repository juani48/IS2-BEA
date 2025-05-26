from data.config import session
from data.query.get import query_get_user

def execute (dni):
    localUser = query_get_user.execute(dni=dni)
    if (localUser is not None):
        localUser.authorized= 1
    else: 
        return "DNI inexistente"
    
    session.commit()
