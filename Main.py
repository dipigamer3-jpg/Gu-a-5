from Funciones import *
from Funciones.ej1 import validar_horario
from Funciones.ej2 import calcular_servicio
from Funciones.ej3 import calcular_recargo_hardware
from Funciones.ej4 import aplicar_descuento
from Funciones.ej5 import impuesto
from Funciones.ej6 import mostrar_orden

valido = False
costo = 0
while True:
    print(f"Usted va a pedir un turno")
    try:
        hora=int(input("Ingrese la hora (0-23): "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido para la hora.")
    try:
        dia=input("Ingrese el día de la semana: ").lower()
    except ValueError:
        print("Error: Por favor, ingrese un día válido con caracteres.")
    valido = validar_horario(hora, dia)
    if valido==True:
        print("El turno es válido.")
    else:
        print("El turno no es válido. Por favor, ingrese una hora entre 8 y 16 en días hábiles.")
    
    tipo_servicio = input("Ingrese el tipo de servicio (mantenimiento, reparacion, urgencia): ").lower()
    costo = calcular_servicio(tipo_servicio)
    costo_base = costo
    if costo > 0:
        print(f"El costo del servicio '{tipo_servicio}' es: ${costo}")
    else:
        print("Tipo de servicio no reconocido. Por favor, ingrese 'mantenimiento', 'reparacion' o 'urgencia'.")
        
    antiguedad_equipo=int(input("Ingrese la antigüedad del equipo en años: "))
    costo_antiguedad = calcular_recargo_hardware(costo, antiguedad_equipo)
    print(f"El recargo por el hardware es de {costo_antiguedad}")
    costo += costo_antiguedad

    try:
        tipo_cliente = input("Ingrese el tipo de cliente (frecuente, estudiante, particular): ").lower()
    except ValueError:
        print("Error: Por favor, ingrese un tipo de cliente válido con caracteres.")
        continue
    if tipo_cliente not in ["frecuente", "estudiante", "particular"]:
        tipo_cliente = "particular"
    descuento=aplicar_descuento(costo, tipo_cliente)
    costo = costo - descuento
    print(f"El descuento aplicado es de {descuento}. El costo total después del descuento es: ${costo}")
    
    impuestoVar = 0
    impuestoVar = impuesto(costo)
    costo = costo + impuestoVar

    print(mostrar_orden(costo, costo_antiguedad, descuento, tipo_servicio, costo_base, impuestoVar))
    break