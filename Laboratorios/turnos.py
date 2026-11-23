
# Laboratorio 3 - Ejercicio 2: Agenda de turnos del dia
# Taller de bicicletas Rueda Libre

print("=== AGENDA DE TURNOS DEL DIA ===")

apertura = int(input("Hora de apertura (0 a 23): "))
cierre = int(input("Hora de cierre (0 a 23): "))

while cierre <= apertura:
    print("El cierre debe ser posterior a la apertura.")
    cierre = int(input("Hora de cierre (0 a 23): "))

duracion = int(input("Minutos por turno: "))

while duracion <= 0:
    print("La duracion debe ser mayor que cero.")
    duracion = int(input("Minutos por turno: "))

inicio = apertura * 60
ultimo_inicio = cierre * 60 - duracion

total_turnos = 0

for minuto in range(inicio, ultimo_inicio + 1, duracion):
    total_turnos += 1

    hora_ini = minuto // 60
    minuto_ini = minuto % 60

    fin = minuto + duracion
    hora_fin = fin // 60
    minuto_fin = fin % 60

    texto_inicio = f"{hora_ini:02d}:{minuto_ini:02d}"
    texto_fin = f"{hora_fin:02d}:{minuto_fin:02d}"

    print(f"Turno {total_turnos}: {texto_inicio} a {texto_fin}")

print(f"Turnos disponibles: {total_turnos}")
