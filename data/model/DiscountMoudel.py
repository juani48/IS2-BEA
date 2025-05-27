from data.config import Base
from sqlalchemy import Column, String, Double, Integer

class DiscountModel(Base):
    __tablename__ = "discount_table"

    discount = Column(Double, nullable=False)
    name = Column(String, primary_key=True)
    need = Column(Integer, nullable=True)

    def __repr__(self):
        return "{" + f"""discount: {self.discount}, name: {self.name}, need: {self.need}""" + "}"
    
    def __init__(self, discount, name, need):
        self.discount = discount
        self.name = name
        self.need = need