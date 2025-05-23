from data.appDataBase import get_all_categories

def usecase_get_all_categories():
    list = get_all_categories()
    return [x.json() for x in list]