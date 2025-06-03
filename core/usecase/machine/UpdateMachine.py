from data.appDataBase import update_machine, get_machine

def usecase_update_machine(patent, mark, model, price_day, ubication, refund, description):
    local_machine = get_machine(patent)

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
    
    update_machine(patent, local_machine)
    
    
    
    