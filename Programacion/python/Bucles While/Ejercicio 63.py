#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
lanzamientos = 0

while lanzamientos < 100:
    lanzamiento = random.randint(1, 6)  
    if lanzamiento == 1:
        cont1 = cont1 + 1
    elif lanzamiento == 2:
        cont2 = cont2 + 1
    elif lanzamiento == 3:
        cont3 = cont3 + 1
    elif lanzamiento == 4:
        cont4 = cont4 + 1
    elif lanzamiento == 5:
        cont5 = cont5 + 1
    else:
        cont6 = cont6 + 1
    lanzamientos = lanzamientos + 1  

print("Resultados de los 100 lanzamientos:")
print("Número 1:", cont1, "veces")
print("Número 2:", cont2, "veces")
print("Número 3:", cont3, "veces")
print("Número 4:", cont4, "veces")
print("Número 5:", cont5, "veces")
print("Número 6:", cont6, "veces")
