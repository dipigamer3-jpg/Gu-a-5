def aplicar_descuento(costo, tipo_cliente):
    if tipo_cliente.lower() == "frecuente": return costo*0.10
    elif tipo_cliente.lower() == "estudiante": return costo*0.20
    elif tipo_cliente.lower() == "particular": return 0
    else: return 0