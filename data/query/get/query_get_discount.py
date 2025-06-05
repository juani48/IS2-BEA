from data.config import session
from data.model.DiscountModel import DiscountModel

def query_get_discount():
    return session.query(DiscountModel).filter_by(name="Points").first()
