from config import Base
from sqlalchemy import Column, Integer, String, Double

class MachineModel(Base):
    __tablename__ = "machine_table"

    patent = Column(Integer, primary_key=True)
    mark = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price_day = Column(Double, nullable=False)
    ubication = Column(String, nullable=False)
    # category = Column() # CF de categoria o rubro
    # refund_strategy = Column() # CF de la estrategia de reembolso

    def __repr__(self):
        return "{" + f"""patent:{self.patent}, 
            mark:{self.mark}, 
            model:{self.model}, 
            price_day:{self.price_day}, 
            ubication:{self.ubication}""" + "}"

    def __init__(self, patent, mark, model, price_day, ubication):
        self.patent = patent
        self.mark = mark
        self.model = model
        self.price_day = price_day
        self.ubication = ubication