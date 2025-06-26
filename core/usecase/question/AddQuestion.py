from data.appDataBase import insert_question
from data.model.QuestionModel import QuestionModel

def usecase_add_question(dni_user , question):
    local_question= QuestionModel (dni_user= dni_user,
                                        question= question
                                   )
    insert_question( question= local_question)


