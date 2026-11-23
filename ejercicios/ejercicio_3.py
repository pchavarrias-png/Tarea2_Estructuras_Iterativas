
# Archivo: ejercicio_3.py
# Curso: Principios de Programación 1
# Autor: Pablo Gerardo Chavarría Segura
# Fecha: 22/11/2026
# Versión: 1.0
# Descripción: Administración de un estacionamiento privado.

# Constantes
CAPACIDAD = 20
TARIFA = 800

# Inicialización de variables
ocupacion = 0
salidas = 0
recaudacion = 0

# Menú principal
while True:
    print("--- ESTACIONAMIENTO PRIVADO ---")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Registrar ingreso
    if opcion == "1":
        if ocupacion < CAPACIDAD:
            ocupacion = ocupacion + 1
            print("Ingreso registrado correctamente.")
        else:
            print("Estacionamiento lleno.")

    # Registrar salida
    elif opcion == "2":
        if ocupacion == 0:
            print("No hay vehículos para registrar salida.")
        else:
            horas = 0

            while horas <= 0:
                try:
                    horas = int(input("Ingrese las horas por cobrar: "))
                    if horas <= 0:
                        print("Error: las horas deben ser mayores que cero.")
                except ValueError:
                    print("Error: ingrese un número entero.")
                    horas = 0

            pago = horas * TARIFA
            ocupacion = ocupacion - 1
            salidas = salidas + 1
            recaudacion = recaudacion + pago

            print("Salida registrada.")
            print("Monto cobrado: ₡", pago)

    # Consultar ocupación
    elif opcion == "3":
        print("Espacios ocupados:", ocupacion)
        print("Espacios libres:", CAPACIDAD - ocupacion)

    # Consultar recaudación
    elif opcion == "4":
        print("Total recaudado: ₡", recaudacion)
        print("Vehículos que han salido:", salidas)

    # Finalizar programa
    elif opcion == "5":
        print("--- RESUMEN FINAL ---")
        print("Vehículos presentes:", ocupacion)
        print("Vehículos que salieron:", salidas)
        print("Recaudación total: ₡", recaudacion)
        print("Programa finalizado.")
        break

    else:
        print("Error: opción no válida.")
