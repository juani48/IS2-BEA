from data.config import session
from data.model.CategorieModel import CategorieModel

def execute():
    return session.query(CategorieModel).filter(CategorieModel.disabled == False).all()