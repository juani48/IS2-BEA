from data.config import session
from data.appDataBase import get_machine

def usecase_update_machine_ubication(patent, new_ubication):
    machine = get_machine(patent)

    if not machine:
        raise Exception("Máquina no encontrada")

    if not new_ubication or new_ubication.strip() == "":
        raise Exception("Ubicación inválida")

    machine.ubication = new_ubication
    session.commit()
