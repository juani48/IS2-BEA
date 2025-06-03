from data.appDataBase import get_all_machines_admin, get_all_machines_by_categorie_admin

# Dicccionarios con booleano y filtro
# {"categorie":"categoria2", "apply": True}
def usecase_get_all_machines_by_admin(categorie_filter, string_filer, price_filter, mark_filter, model_filter):
    if (categorie_filter.get("apply")):
        list = get_all_machines_by_categorie_admin(categorie_filter.get("categorie"))
    else:
        list = get_all_machines_admin()

    list = __string_filter__(string_filer, list)
    list = __price_filter__(price_filter, list)
    list = __mark_filter__(mark_filter, list)
    list = __model_filter__(model_filter, list)
    return [ x.json() for x in list ]

def __string_filter__(string_filer, list):
    if (string_filer.get("apply") and string_filer.get("string") != ""):
        new_list = []

        str = string_filer.get("string")
        for i in range(0, len(list)):
            if list[i].include(str):
                new_list.append(list[i])
        return new_list 
    return list

def __price_filter__(price_filter, list):
    if (price_filter.get("apply")):
        list = [x for x in list if price_filter.get("price") >= x.price_day]
    return list

def __mark_filter__(mark_filter, list):
    if (mark_filter.get("apply")):
        list = [x for x in list if mark_filter.get("mark").lower() in x.mark.lower()] # stream in python
    return list

def __model_filter__(model_filter, list):
    if (model_filter.get("apply")):
        list = [x for x in list if model_filter.get("model").lower() in x.model.lower()] # stream in python
    return list