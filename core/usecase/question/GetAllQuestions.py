from data.appDataBase import get_all_questions

def usecase_get_all_questions():
    list = get_all_questions()
    return [x.json() for x in list]