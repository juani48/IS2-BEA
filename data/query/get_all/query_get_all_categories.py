from data.config import session
from data.model.CategorieModel import CategorieModel

def execute():
    return session.query(CategorieModel).all()

#.filter(CategorieModel.disabled == False) le saque eso para que me de todas