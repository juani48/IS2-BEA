#from data.config import session
#from data.model.CategorieModel import CategorieModel
#from data.model.MachineCategorieModel import MachineCategorieModel

#def execute(categorie):
#    local_categorie = session.get(CategorieModel, categorie)
    
#    local_machine_categorie = session.query(MachineCategorieModel).filter(MachineCategorieModel.categorie_id == categorie).all()
#    if(local_machine_categorie != None):
#        raise Exception("No es posible eliminar la categoria, existen maquinas con dicha categoria")
    
#    local_categorie.disabled = True
#    session.commit()
    
from data.config import session
from data.model.CategorieModel import CategorieModel
from data.model.MachineCategorieModel import MachineCategorieModel

def execute(categorie):
    # Buscar la categoría en la base
    local_categorie = session.get(CategorieModel, categorie)
    if local_categorie is None:
        raise Exception("Categoría no encontrada")

    # Buscar todas las asociaciones de máquinas a esa categoría
    asociaciones = session.query(MachineCategorieModel).filter(
        MachineCategorieModel.categorie_id == categorie
    ).all()

    # Por cada máquina asociada, verificar si tiene al menos otra categoría
    for asociacion in asociaciones:
        cantidad = session.query(MachineCategorieModel).filter(
            MachineCategorieModel.machine_id == asociacion.machine_id
        ).count()
        if cantidad <= 1:
            raise Exception("No se puede deshabilitar una categoría si hay máquinas que quedarían sin categoría")

    # Si pasó todas las validaciones, deshabilitamos la categoría
    local_categorie.disabled = True
    session.commit()
