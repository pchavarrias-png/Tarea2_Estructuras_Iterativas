
# Problema 4: Promedio de tres notas
# Laboratorio 1 - Mis primeros programas en Python

# Entrada
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))

# Proceso
promedio = (nota_1 + nota_2 + nota_3) / 3

# Salida
print(f"El promedio de {nombre_estudiante} es: {promedio:.2f}")
