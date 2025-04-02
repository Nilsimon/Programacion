#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
random= int(random.randint(0,1000))
var1=0
while var1!=random:
    var1=int(input("Introduce un numero 0-1000:"))
    if var1>random:
        print("El numero que has introducido es mayor")
    if var1<random:
        print("El numero que has introducido es menor")
print("Has acertado")
