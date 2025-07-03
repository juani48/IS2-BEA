from data.config import session
from data.model.CommentaryModel import CommentaryModel

def execute(date):
    local_commentary= session.get(CommentaryModel,date)
    return local_commentary