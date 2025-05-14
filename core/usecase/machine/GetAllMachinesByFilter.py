from data.appDataBase import get_all_machines, get_all_machines_by_categorie

# Dicccionarios con booleano y filtro
def usecase_get_all_machines_by(categorie_filter, price_filter, mark_filter, model_filter):
    if (categorie_filter.apply):
        list = get_all_machines_by_categorie(categorie_filter.categorie)
    else:
        list = get_all_machines()

    list = _price_filter(price_filter, list)
    list = _mark_filter(mark_filter, list)
    list = _model_filter(model_filter, list)
    return list

def _price_filter(price_filter, list):
    if (price_filter.apply):
        list = [x for x in list if price_filter.price == x.price]
    return list

def _mark_filter(mark_filter, list):
    if (mark_filter.apply):
        list = [x for x in list if mark_filter.mark.lower() in x.mark.lower()] # stream in python
    return list

def _model_filter(model_filter, list):
    if (model_filter.apply):
        list = [x for x in list if model_filter.model.lower() in x.model.lower()] # stream in python
    return list
