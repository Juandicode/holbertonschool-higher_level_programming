"""

1. Variables y Operadores Básicos
Ejercicio 1: Calcula el área de un triángulo (base × altura / 2).

python
Copy
base = 5
altura = 10
area = (base * altura) / 2
print("El área del triángulo es:", area)
Ejercicio 2: Convierte grados Celsius a Fahrenheit (F = C × 9/5 + 32).

python
Copy
celsius = 30
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C son {fahrenheit}°F")

2. Condicionales (if-elif-else)
Ejercicio 3: Determina si un número es positivo, negativo o cero.

python
Copy
numero = -5
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")
Ejercicio 4: Verifica si un número es par o impar.

python
Copy
numero = 4
if numero % 2 == 0:
    print("Par")
else:
    print("Impar")

    
3. Bucles (for, while)
Ejercicio 5: Imprime los números del 1 al 10 usando un bucle for.

python
Copy
for i in range(1, 11):
    print(i)
Ejercicio 6: Suma todos los números del 1 al 100 con un bucle while.

python
Copy
suma = 0
i = 1
while i <= 100:
    suma += i
    i += 1
print("La suma es:", suma)


4. Listas y Diccionarios
Ejercicio 7: Encuentra el número más grande en una lista.

python
Copy
lista = [3, 7, 2, 10, 5]
maximo = max(lista)  # Opción fácil
# O con un bucle:
maximo = lista[0]
for num in lista:
    if num > maximo:
        maximo = num
print("El máximo es:", maximo)
Ejercicio 8: Crea un diccionario con nombres y edades, luego imprime solo los nombres.

python
Copy
personas = {"Ana": 25, "Luis": 30, "Carlos": 20}
for nombre in personas.keys():
    print(nombre)

    
    
5. Funciones
Ejercicio 9: Crea una función que devuelva el factorial de un número (n! = 1 × 2 × ... × n).

python
Copy
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))  # 120
Ejercicio 10: Función que verifica si una palabra es un palíndromo (se lee igual al revés).

python
Copy
def es_palindromo(palabra):
    return palabra == palabra[::-1]

print(es_palindromo("reconocer"))  # True


)"""