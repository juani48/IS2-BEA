from datetime import datetime

def current_date_format(date):
    months = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )
    day = date.day
    month = months[date.month - 1]
    year = date.year
    hour = date.hour
    minute = date.minute
    second = date.second

    message = "{} de {} del {} - {:02d}:{:02d}:{:02d}".format(day, month, year, hour, minute, second)
    return message