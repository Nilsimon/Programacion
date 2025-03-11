#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
var1=0
numeroaleatorio= int(random.randint(1,5))
while var1!=numeroaleatorio:
    var1= int(input("Introduce un numero:"))
    if var1!=numeroaleatorio:
        print("Incorrecto")
print("Numero correcto")