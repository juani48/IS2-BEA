from data.config import Base
from sqlalchemy import Column, Integer, Double, String, Boolean

class MachineModel(Base):
    __tablename__ = "machine_table"

    patent = Column(String, primary_key=True)
    mark = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price_day = Column(Double, nullable=False)
    ubication = Column(String, nullable=False)
    refund = Column(Double, nullable=False)  # reembolso
    disable = Column(Boolean, nullable=False, default=False)

    description = Column(String, nullable=True)
    creation_date = Column(String, nullable=False)
    
    under_maintenance = Column(Boolean, nullable=False, default=False)

    # stock?
    # variable string para mostrar el estado (disponible, o en mantenimiento)

    def __repr__(self):
        return "{" + f"""patent:{self.patent}, mark:{self.mark}, model:{self.model}, price_day:{self.price_day}, ubication:{self.ubication}, refund: {self.refund}, disable: {self.disable}, creation_date: {self.creation_date}, under_maintenance: {self.under_maintenance}""" + "}"

    def json(self):
        return {
            "patent": self.patent,
            "mark": self.mark,
            "model": self.model,
            "price_day": self.price_day,
            "ubication": self.ubication,
            "refund": self.refund,
            "disable": self.disable,
            "description": self.description,
            "creation_date": self.creation_date,
            "under_maintenance": self.under_maintenance
        }

    def include(self, string):
        str = string.lower()
        return (str in self.patent.lower() or
                str in self.mark.lower() or
                str in self.model.lower() or
                str in self.ubication.lower() or
                str in self.description.lower())
        # if self.description:
        #     return str in self.description.lower()

    def __init__(self, patent, mark, model, price_day, ubication, refund, description, creation_date):
        self.patent = patent
        self.mark = mark
        self.model = model
        self.price_day = price_day
        self.ubication = ubication
        self.refund = refund
        self.disable = False
        self.description = description
        self.creation_date = creation_date
        self.under_maintenance = False
