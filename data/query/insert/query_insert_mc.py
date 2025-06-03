from data.config import session
from data.model.MachineCategorieModel import MachineCategorieModel

#def execute(patent, categorie, machine_categorie):
#    local_mc = session.get(MachineCategorieModel, (patent, categorie))
#    if (local_mc != None):
#        raise Exception("La maquina ya tiene esta categoria")
#    session.add(machine_categorie)
#    session.commit()

def execute(patent, categorie, machine_categorie_list):
    for mc in machine_categorie_list:
        # Validar si ya existe la relación
        local_mc = session.get(MachineCategorieModel, (mc.machine_id, mc.categorie_id))
        if local_mc:
            raise Exception(f"La máquina {mc.machine_id} ya tiene la categoría {mc.categorie_id}")
        session.add(mc)
    
    session.commit()