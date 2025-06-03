from data.config import session
from data.model.DiscountModel import DiscountModel

def execute():
    session.add(DiscountModel(
        10, "Employee", None
    ))

    session.add(DiscountModel(
        discount=15, name="Points", need=5
    ))
    session.commit