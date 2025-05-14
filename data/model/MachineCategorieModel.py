from data.config import Base
from sqlalchemy import Column, String, ForeignKey

class MachineCategorieModel(Base):
    __tablename__ = "machine_categorie_table"
    
    machine_id = Column(String, ForeignKey("machine_table.patent"), primary_key=True, nullable=False)
    categorie_id = Column(String, ForeignKey("categorie_table.name"), primary_key=True, nullable=False)

    def __repr__(self):
        return "{" + f"""machine_id: {self.machine_id}, categorie_id: {self.categorie_id}""" + "}"
    
    def __init__(self, machine_id, categorie_id):
        self.machine_id = machine_id
        self.categorie_id = categorie_id