from data.appDataBase import insert_question
from data.model.QuestionModel import QuestionModel

def usecase_add_question(user_name, question):
    local_question= QuestionModel (name_user= user_name, 
                                     question= question,
                                        answer=None,
                                            name_employee="Pendiente"
                                   )
    insert_question( question= local_question)


