from data.config import session
from data.model.CommentaryModel import CommentaryModel

def execute(machine_number):
    commentarys_list = session.query(CommentaryModel).filter(CommentaryModel.machine_number == machine_number ).all()
    
    return commentarys_list