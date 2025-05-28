from data.appDataBase import get_all_requests

def usecase_get_all_requests():
    requests_list = get_all_requests()
    return [ x.json() for x in requests_list ]