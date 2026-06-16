def validar_horario(hora,dia):
    if dia in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
        if 8 <= hora < 16:
            return True
    return False