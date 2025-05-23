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
    
    # stock?

    def __repr__(self):
        return "{" + f"""patent:{self.patent}, mark:{self.mark}, model:{self.model}, price_day:{self.price_day}, ubication:{self.ubication}, refund: {self.refund}, disable: {self.disable}""" + "}"

    def json(self):
        return {
            "patent": self.patent,
            "mark": self.mark,
            "model": self.model,
            "price_day": self.price_day,
            "ubication": self.ubication,
            "refund": self.refund,
            "disable": self.disable
            # "description": self.description,
            # "image": self.image
        }

    def include(self, string):
        str = string.lower()
        return (str in self.patent.lower() or
                str in self.mark.lower() or
                str in self.model.lower() or
                str in self.ubication.lower())
        # if self.description:
        #     return str in self.description.lower()

    def __init__(self, patent, mark, model, price_day, ubication, refund):
        self.patent = patent
        self.mark = mark
        self.model = model
        self.price_day = price_day
        self.ubication = ubication
        self.refund = refund
        self.disable = False
        # self.description = description
        # self.image = image
