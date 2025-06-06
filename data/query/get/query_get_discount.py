from data.config import session
from data.model.DiscountModel import DiscountModel

def query_get_discount(name):
    return session.get(DiscountModel, name)
