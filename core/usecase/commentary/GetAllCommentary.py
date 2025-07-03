from data.appDataBase import get_all_commentarys, get_user
import json

def usecase_get_all_commentarys(machine_patent):
    all_comments = get_all_commentarys(machine_patent)

    # Diccionario para acceso rápido por date
    comment_dict_by_date = {c.date: c for c in all_comments}

    # Recolectar todos los 'date' que son respuestas
    dates_that_are_answers = set()
    for c in all_comments:
        if c.answer:
            try:
                answer_ids = json.loads(c.answer)
                dates_that_are_answers.update(answer_ids)
            except:
                pass

    # Función recursiva para construir árbol de respuestas
    def build_comment_tree(comment):
        comment_json = comment.json()

        # ➕ Agregar info del usuario
        user = get_user(comment.dni)
        if user:
            comment_json["name"] = user.name
            comment_json["lastname"] = user.lastname
        else:
            comment_json["name"] = None
            comment_json["lastname"] = None

        # ➕ Manejo de respuestas
        answers_list = []
        if comment.answer:
            try:
                answer_ids = json.loads(comment.answer)
                for aid in answer_ids:
                    child = comment_dict_by_date.get(aid)
                    if child:
                        answers_list.append(build_comment_tree(child))
            except:
                pass

        comment_json["answers"] = answers_list
        return comment_json

    # Comentarios raíz (no son respuestas de otro)
    root_comments = [c for c in all_comments if c.date not in dates_that_are_answers]

    return [build_comment_tree(c) for c in root_comments]
