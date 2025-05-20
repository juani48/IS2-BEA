from data.config import Base
from sqlalchemy import Column, String, Boolean

class CategorieModel(Base):
    __tablename__ = "categorie_table"
    
    name = Column(String, primary_key=True, nullable=False)
    disabled = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return "{" + f"""name: {self.name}, disable: {self.disabled}""" + "}"
    
    def json(self):
        return {
            "name": self.name,
            "disable": self.disabled
        }

    def __init__(self, name):
        self.name = name
        self.disabled = False
