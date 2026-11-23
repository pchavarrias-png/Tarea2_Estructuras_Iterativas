
# Laboratorio 2 - Ciclos for sin colecciones
# Simulador de ahorro - Cooperativa Ahorro Andino

BONO_FIDELIDAD = 0.01

# Paso 1: Datos del socio
deposito = float(input("Deposito mensual ($): "))
meses = int(input("Plazo (meses): "))

while meses < 1:
    print("El plazo debe ser mayor que cero.")
    meses = int(input("Plazo (meses): "))

tasa_anual = float(input("Tasa de interes anual (%): "))
meta = float(input("Meta de ahorro ($): "))

tasa_mensual = tasa_anual / 100 / 12

# Paso 2: Inicializar acumuladores
saldo = 0.0
total_depositado = 0.0
total_intereses = 0.0
total_bonos = 0.0

meta_alcanzada = False
mes_meta = 0

print("\n=== SIMULACION DE AHORRO ===")
print(f"{'Mes':>4} {'Deposito':>10} {'Interes':>10} {'Bono':>10} {'Saldo':>12}")

# Paso 3: Simular cada mes
for mes in range(1, meses + 1):

    # Reto final: aumentar el deposito cada 12 meses
    if mes > 1 and (mes - 1) % 12 == 0:
        deposito = deposito * 1.05

    saldo = saldo + deposito
    total_depositado = total_depositado + deposito

    interes = saldo * tasa_mensual
    saldo = saldo + interes
    total_intereses = total_intereses + interes

    bono = 0.0

    if mes % 12 == 0:
        bono = saldo * BONO_FIDELIDAD
        saldo = saldo + bono
        total_bonos = total_bonos + bono

    print(f"{mes:>4} {deposito:>10.2f} {interes:>10.2f} {bono:>10.2f} {saldo:>12.2f}")

    # Paso 4: Guardar el primer mes que alcanza la meta
    if not meta_alcanzada and saldo >= meta:
        meta_alcanzada = True
        mes_meta = mes

# Paso 5: Resumen final
print("\n=== RESUMEN DEL PLAN ===")
print(f"Total depositado: ${total_depositado:,.2f}")
print(f"Intereses ganados: ${total_intereses:,.2f}")
print(f"Bonos recibidos: ${total_bonos:,.2f}")
print(f"Saldo final: ${saldo:,.2f}")

if meta_alcanzada:
    print(f"La meta de ${meta:,.2f} se alcanzo en el mes {mes_meta}.")
else:
    faltante = meta - saldo
    print(f"La meta no se alcanzo. Faltan ${faltante:,.2f}.")

# Paso 6: Comparacion de tasas con ciclos anidados
print("\n=== COMPARACION DE TASAS ===")

for tasa in range(4, 13, 2):
    tasa_mensual_comparacion = tasa / 100 / 12
    saldo_comparacion = 0.0
    deposito_comparacion = deposito / (1.05 ** ((meses - 1) // 12))

    for mes in range(1, meses + 1):

        if mes > 1 and (mes - 1) % 12 == 0:
            deposito_comparacion = deposito_comparacion * 1.05

        saldo_comparacion = saldo_comparacion + deposito_comparacion
        interes_comparacion = saldo_comparacion * tasa_mensual_comparacion
        saldo_comparacion = saldo_comparacion + interes_comparacion

        if mes % 12 == 0:
            saldo_comparacion = saldo_comparacion * (1 + BONO_FIDELIDAD)

    print(f"{tasa}% anual -> saldo final ${saldo_comparacion:,.2f}")
