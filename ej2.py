def calcular_servicio(tipo_servicio):
    if tipo_servicio == "mantenimiento": return 5000
    elif tipo_servicio == "reparacion": return 9000
    elif tipo_servicio == "urgencia": return 14000
    else: return 0