from data.config import session
from data.model.CategorieModel import CategorieModel

def execute(categorie):
    local_categorie = session.get(CategorieModel, categorie)
    local_categorie.disabled = False
    session.commit()
    