from data.appDataBase import update_machine, get_machine, delete_machine_categorie, insert_machine_categorie
from data.model.MachineCategorieModel import MachineCategorieModel

def usecase_update_machine(patent, categorie, mark, model, price_day, ubication, refund, description, creation_date):
    local_machine = get_machine(patent)

    if(len(categorie) != 0):
        delete_machine_categorie(patent)
        for c in categorie:
            insert_machine_categorie(patent, c, MachineCategorieModel(patent, c))
    if(mark != None and mark != ""):
        local_machine.mark = mark
    if(model != None and model != ""):
        local_machine.model = model
    if(price_day != None and price_day > 0):
        local_machine.price_day = price_day
    if(refund != None):
        local_machine.refund = refund
    if(ubication != None and ubication != ""):
        local_machine.ubication = ubication
    if(description != None and description != ""):
        local_machine.description = description
    if(creation_date != None and creation_date != ""):
        local_machine.creation_date = creation_date
    
    update_machine(patent, local_machine)
    
    
    
    