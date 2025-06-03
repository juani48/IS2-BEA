from data.appDataBase import get_all_categories

def usecase_get_all_categories():
    list = get_all_categories()
    new_list = []
    for x in list:
        if x.disabled == False:
            new_list.append(x.name)
    return new_list