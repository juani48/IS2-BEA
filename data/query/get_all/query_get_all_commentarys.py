from data.config import session
from data.model.CommentaryModel import CommentaryModel

def execute(machine_patent):
    commentarys_list = session.query(CommentaryModel).filter(CommentaryModel.machine_patent == machine_patent ).all()
    
    return commentarys_list