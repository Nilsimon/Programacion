#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma = 0

numero = int(input("Introduce un número (-99 para salir): "))

mayor = numero
menor = numero
while numero != -99:
    suma += numero
    if numero == 0:
        ceros += 1
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    numero = int(input("Introduce un número (-99 para salir): "))

print(f"Total de pares: {pares}")
print(f"Total de impares: {impares}")
print(f"Total de positivos: {positivos}")
print(f"Total de negativos: {negativos}")
print(f"Total de ceros: {ceros}")
print(f"Suma total de los números: {suma}")
print(f"Mayor número: {mayor}")
print(f"Menor número: {menor}")
