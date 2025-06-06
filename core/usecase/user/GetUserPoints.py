from data.appDataBase import get_user, get_discount

def usecase_get_user_points(client_id):
    user = get_user(client_id)
    discount = get_discount("Points").discount
    need = get_discount("Points").need

    return { "points": user.points, "discount": discount, "need": need }