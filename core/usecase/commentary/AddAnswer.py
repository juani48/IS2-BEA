from data.model.CommentaryModel import CommentaryModel
from data.appDataBase import insert_commentary,insert_answer

def usecase_add_answer(date,dni,commentaryStr,machine_patent,answerID,dateCommentary):

    local_commentary= CommentaryModel( date= date,
                                       dni=dni,
                                       commentary= commentaryStr,
                                       machine_patent=machine_patent,
                                       answer= answerID 
                                )
    
    insert_commentary(machine_patent= machine_patent, commentary= local_commentary)
    insert_answer(dateID= dateCommentary,answerID= date)