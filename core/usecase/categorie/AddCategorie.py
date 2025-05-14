from data.model.CategorieModel import CategorieModel
from data.appDataBase import insert_categorie

def usecase_add_categorie(categorie):
    if (categorie == ""):
        raise Exception("El nombre de la categoria no puede estar vacio")
    c = CategorieModel(
        name=categorie
    )
    insert_categorie(name=categorie, categorie=c)