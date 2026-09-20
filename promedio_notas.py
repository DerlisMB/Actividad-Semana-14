# Función que recibe tres notas como parámetros y devuelve el promedio
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio   # Aquí está el return 

# Programa principal
print("=== Calculadora de Promedio de Notas ===")

# Pedimos las tres notas al usuario
n1 = float(input("Ingresa la primera nota: "))
n2 = float(input("Ingresa la segunda nota: "))
n3 = float(input("Ingresa la tercera nota: "))

# Llamamos a la función y guardamos el resultado
resultado = calcular_promedio(n1, n2, n3)

# Mostramos el resultado
print(f"\nEl promedio de las tres notas es: {resultado:.2f}")   