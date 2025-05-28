from data.config import session
from data.model.DiscountMoudel import DiscountModel

def exectue(name):
    return session.get(DiscountModel, name)