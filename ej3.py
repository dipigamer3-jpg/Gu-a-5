def calcular_recargo_hardware(costo, antiguedad_equipo):
    if antiguedad_equipo >=0 and antiguedad_equipo <=3: return 0
    elif antiguedad_equipo >=4 and antiguedad_equipo <=7:
        return 1500
    elif antiguedad_equipo >7:
        total = (costo * 100) /25
        adicional = total + 2000
        return adicional