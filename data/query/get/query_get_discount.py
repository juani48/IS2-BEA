from data.config import session
from data.model.DiscountModel import DiscountModel

def exectue(name):
    return session.get(DiscountModel, name)