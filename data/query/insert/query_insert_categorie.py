from data.config import session
from data.model.CategorieModel import CategorieModel

def execute(name, categorie):
    local_categorie = session.query(CategorieModel).filter(CategorieModel.name == name).first()
    if(local_categorie != None):
        raise Exception("Categoria existente")
    session.add(categorie)
    session.commit()