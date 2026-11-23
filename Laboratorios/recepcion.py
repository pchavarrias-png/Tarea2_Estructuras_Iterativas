
# Laboratorio 3 - Ejercicio 1
# Recepcion del taller Rueda Libre

TARIFA_HORA = 32.00

bicis_recibidas = 0

while True:
    print("\n--- RECEPCION - TALLER RUEDA LIBRE ---")
    print("1. Recibir bicicleta")
    print("2. Ver horario de atencion")
    print("3. Cotizar mano de obra")
    print("0. Cerrar recepcion")

    opcion = input("Opcion: ").strip()

    if opcion == "1":
        cliente = input("Nombre del cliente: ").strip()

        if cliente == "":
            print("El nombre no puede quedar vacio.")
            continue

        bicis_recibidas += 1
        print(f"Bicicleta {bicis_recibidas} recibida a nombre de {cliente}.")

    elif opcion == "2":
        print("Horario: de 8:00 a 12:00 y de 13:00 a 17:00.")

    elif opcion == "3":
        texto = input("Minutos de trabajo estimados: ").strip()

        if not texto.isdigit():
            print("Escriba los minutos con numeros enteros.")
            continue

        minutos = int(texto)
        horas = minutos // 60
        minutos_restantes = minutos % 60
        costo = minutos / 60 * TARIFA_HORA

        print(f"Trabajo de {horas} h {minutos_restantes} min.")
        print(f"Mano de obra: ${costo:.2f}")

    elif opcion == "0":
        confirmar = input("Cerrar la recepcion (s/n): ").strip().lower()

        if confirmar == "s":
            print(f"Recepcion cerrada. Bicicletas recibidas hoy: {bicis_recibidas}.")
            break

    else:
        print("Opcion no valida.")
