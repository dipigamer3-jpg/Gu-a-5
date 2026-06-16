def calcular_recargo_hardware(costo, antiguedad_equipo):
    if antiguedad_equipo >=0 and antiguedad_equipo <=3: return costo
    elif antiguedad_equipo >=4 and antiguedad_equipo <=7:
        total = costo + 1500
        return total
    elif antiguedad_equipo >7:
        total = (costo * 100) /25
        adicional = total + 2000
        return adicional