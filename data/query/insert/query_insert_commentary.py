from data.config import session
from data.model.MachineModel import MachineModel
from data.model.CommentaryModel import CommentaryModel

def execute(machine_patent,commentary):
    local_machine = session.get(MachineModel, machine_patent)
    if(local_machine == None):
        raise Exception("Máquina inexistente.")
    session.add(commentary)
    session.commit()