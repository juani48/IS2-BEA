from data.model.CommentaryModel import CommentaryModel
from data.appDataBase import insert_commentary

def usecase_add_commentary(date,dni,commentaryStr,machine_patent,answer):

    local_commentary= CommentaryModel( date= date,
                                       dni=dni,
                                       commentary= commentaryStr,
                                       machine_patent=machine_patent,
                                       answer= answer 
                                )
    
    insert_commentary(machine_patent= machine_patent, commentary= local_commentary)