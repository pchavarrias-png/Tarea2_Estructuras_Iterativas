
# Laboratorio 1 - Ciclos while con bandera y contador
# Control de calidad - Cafe del Valle

CODIGO_SUPERVISOR = "CAFE2026"
MAX_INTENTOS = 3
PESO_OBJETIVO = 500
TOLERANCIA = 10
MAX_CONSECUTIVAS = 3

# Paso 1: Acceso del supervisor
intentos = 0
acceso_concedido = False

while intentos < MAX_INTENTOS and not acceso_concedido:
    codigo = input("Codigo de supervisor: ")
    intentos += 1

    if codigo == CODIGO_SUPERVISOR:
        acceso_concedido = True
    else:
        restantes = MAX_INTENTOS - intentos
        print(f"Codigo incorrecto. Intentos restantes: {restantes}")

if not acceso_concedido:
    print("Acceso bloqueado. Avise al jefe de planta.")

else:
    print("Acceso concedido. Inicie el registro (0 para terminar).")

    # Paso 2: Inicializar variables
    total_bolsas = 0
    aceptadas = 0
    defectuosas = 0
    consecutivas = 0
    peso_acumulado = 0
    terminar = False
    linea_detenida = False

    # Reto final: peso minimo y maximo
    peso_minimo = 0
    peso_maximo = 0

    # Paso 3: Registrar y validar bolsas
    while not terminar and not linea_detenida:
        peso = float(input(f"Peso de la bolsa {total_bolsas + 1} (g): "))

        while peso < 0:
            print("El peso no puede ser negativo.")
            peso = float(input(f"Peso de la bolsa {total_bolsas + 1} (g): "))

        if peso == 0:
            terminar = True
        else:
            total_bolsas += 1
            peso_acumulado += peso

            # Actualizar minimo y maximo
            if total_bolsas == 1:
                peso_minimo = peso
                peso_maximo = peso
            else:
                if peso < peso_minimo:
                    peso_minimo = peso
                if peso > peso_maximo:
                    peso_maximo = peso

            # Paso 4: Clasificar la bolsa
            diferencia = peso - PESO_OBJETIVO

            if diferencia < 0:
                diferencia = -diferencia

            if diferencia <= TOLERANCIA:
                aceptadas += 1
                consecutivas = 0
                print("OK")
            else:
                defectuosas += 1
                consecutivas += 1
                print("DEFECTUOSA")

                # Paso 5: Alarma
                if consecutivas == MAX_CONSECUTIVAS:
                    print(f"ALERTA: {consecutivas} bolsas defectuosas seguidas.")
                    linea_detenida = True

    # Paso 6: Reporte del turno
    print("\n=== REPORTE DEL TURNO ===")
    print(f"Bolsas revisadas: {total_bolsas}")
    print(f"Aceptadas: {aceptadas}")
    print(f"Defectuosas: {defectuosas}")

    if total_bolsas > 0:
        porcentaje = defectuosas / total_bolsas * 100
        promedio = peso_acumulado / total_bolsas

        print(f"% defectuosas: {porcentaje:.1f} %")
        print(f"Peso promedio: {promedio:.1f} g")
        print(f"Peso minimo: {peso_minimo:.1f} g")
        print(f"Peso maximo: {peso_maximo:.1f} g")
    else:
        print("No se registraron bolsas.")

    if linea_detenida:
        print("ALERTA: Linea detenida por 3 bolsas defectuosas seguidas.")
        print("Revise la dosificadora.")
