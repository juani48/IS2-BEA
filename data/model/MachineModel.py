from data.config import Base
from sqlalchemy import Column, Integer, Double, String, Boolean

class MachineModel(Base):
    __tablename__ = "machine_table"

    patent = Column(String, primary_key=True)
    mark = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price_day = Column(Double, nullable=False)
    ubication = Column(String, nullable=False)
    refund = Column(Double, nullable=False) # reembolso
    disable = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return "{" + f"""patent:{self.patent}, mark:{self.mark}, model:{self.model}, price_day:{self.price_day}, ubication:{self.ubication}, refund: {self.refund}, disable: {self.disable}""" + "}"

    def __init__(self, patent, mark, model, price_day, ubication, refund):
        self.patent = patent
        self.mark = mark
        self.model = model
        self.price_day = price_day
        self.ubication = ubication
        self.refund = refund
        self.disable = False