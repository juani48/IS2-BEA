from data.model.CommentaryModel import CommentaryModel
from data.appDataBase import insert_commentary

def usecase_add_commentary(machine_patent,commentaryStr,dni):

    local_commentary= CommentaryModel( dni=dni,
                                commentary= commentaryStr,
                                machine_patent=machine_patent 
                                )
    
    insert_commentary(machine_patent= machine_patent, commentary= local_commentary)