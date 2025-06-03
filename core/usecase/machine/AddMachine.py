from data.model.MachineModel import MachineModel
from data.model.MachineCategorieModel import MachineCategorieModel
from data.appDataBase import insert_machine, insert_machine_categorie

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
    insert_machine(patent, machine)

    for c in categorie:
        mc = MachineCategorieModel(
            machine_id=patent,
            categorie_id=c
        )
        insert_machine_categorie(patent, c, mc)
        


def validator(patent, mark, model, price_day, ubication, refund, categorie):
    if (patent == ""):
        raise Exception("La patente no puede estar vacia.")
    if (mark == ""):
        raise Exception("La marca no puede estar vacia.")
    if (model == ""):
        raise Exception("El modelo no puede estar vacio.")
    if (price_day == 0 or price_day == None):
        raise Exception("El precio por dia no puede estar vacio.")
    if (ubication == ""):
        raise Exception("La ubicacion no puede estar vacia.")
    if (refund == None):
        raise Exception("El reembolso no puede estar vacio.")
    if (len(categorie) == 0):
        raise Exception("La categoria no puede estar vacia.")
    