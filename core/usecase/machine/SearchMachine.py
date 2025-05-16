from data.appDataBase import get_all_machines

def usecase_search_machine(patent):
    machines = get_all_machines()
    machine = machines.index(patent)

    return machine
            