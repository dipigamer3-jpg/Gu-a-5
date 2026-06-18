def mostrar_orden(costo, costo_antiguedad, descuento, tipo_servicio, costo_base, impuestoVar):
    print("\n--- Detalles de la Orden ---")
    print(f"Servicio a realizar: {tipo_servicio}")
    print(f"Costo base: ${costo_base}")
    print(f"Recargo por complejidad: ${costo_antiguedad}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"Impuesto aplicado: ${impuestoVar}")
    print("------------------------------")
    print(f"Total neto a pagar: ${costo}")