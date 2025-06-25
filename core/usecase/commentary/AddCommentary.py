from data.model.CommentaryModel import CommentaryModel
from data.appDataBase import insert_commentary

def usecase_add_commentary(machine_number,commentaryStr,name):

    local_commentary= CommentaryModel( name=name,
                                commentary= commentaryStr,
                                machine_number=machine_number
                                )
    
    insert_commentary(machine_number= machine_number, commentary= local_commentary)