from data.appDataBase import get_all_machines

def usecase_get_all_machines_by(name):
    list = get_all_machines()
    new_list = []
    if(name != ""):
        for i in range(0, len(list)):
            if list[i].include(name):
                new_list.append(list[i])
    return [ x.json() for x in new_list ]
