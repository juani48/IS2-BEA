from data.config import session
from data.model.CategorieModel import CategorieModel
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(categorie):
    local_categorie = session.get(CategorieModel, categorie)
    
    local_machine_categorie = session.query(MachineCategorieModel).filter(MachineCategorieModel.categorie_id == categorie).all()
    if(local_machine_categorie != None):
        raise Exception("No es posible eliminar la cateogira, existen maquinas con dicha categoria")
    
    local_categorie.disabled = True
    session.commit()
    