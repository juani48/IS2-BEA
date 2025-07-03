from data.config import session
import json 
from data.model.CommentaryModel import CommentaryModel

def execute(dateID, answerID):
    local_commentary = session.get(CommentaryModel, dateID)

    if local_commentary is None:
        raise Exception("Comentario inexistente.")

    try:
        current_answers = json.loads(local_commentary.answer or "[]")
    except json.decoder.JSONDecodeError:
        current_answers = [local_commentary.answer] if local_commentary.answer else []

    # Asegurar que el answerID sea un string serializable
    if answerID is not None:
        answerID = str(answerID)

        if answerID not in current_answers:
            current_answers.append(answerID)

    local_commentary.answer = json.dumps(current_answers)
    session.commit()

    