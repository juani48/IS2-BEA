from data.appDataBase import enable_user,delete_user

def usecase_reply_request(reply,dni):
    if (reply):
        enable_user(dni=dni)
    else:
        delete_user(dni=dni)

