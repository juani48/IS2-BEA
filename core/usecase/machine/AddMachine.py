from data.model.MachineModel import MachineModel
from data.model.MachineCategorieModel import MachineCategorieModel
from data.appDataBase import insert_machine

def usecase_add_machine(patent, mark, model, price_day, ubication, refund, categorie, description):
    validator(patent, mark, model, price_day, ubication, refund, categorie)

    machine = MachineModel(
        patent=patent,
        mark=mark,
        model=model,
        price_day=price_day,
        ubication=ubication,
        refund=refund,
        description=description,
    )

    # Crear una lista de relaciones máquina-categoría
    machine_categorie_list = [
        MachineCategorieModel(machine_id=patent, categorie_id=cat) for cat in categorie
    ]
    

    insert_machine(
        patent=patent,
        categorie=categorie,
        machine=machine,
        machine_categorie=machine_categorie_list  # Ahora pasás una lista
    )


def validator(patent, mark, model, price_day, ubication, refund, categorie):
    if (patent == ""):
        raise Exception("La patente no puede estar vacia")
    if (mark == ""):
        raise Exception("La marca no puede estar vacia")
    if (model == ""):
        raise Exception("El modelo no puede estar vacio")
    if (price_day == 0 or price_day == None):
        raise Exception("El precio por dia no puede estar vacio")
    if (ubication == ""):
        raise Exception("La ubicacion no puede estar vacia")
    if (refund == None):
        raise Exception("El reembolso no puede estar vacio")
    if not categorie:
        raise Exception("La categoría no puede estar vacía")
