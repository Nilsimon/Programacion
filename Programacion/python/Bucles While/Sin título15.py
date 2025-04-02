#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
var1=0
intentos=0
numeroaleatorio= int(random.randint(1,5))
while var1!=numeroaleatorio and intentos<3:
    var1= int(input("Introduce un numero:"))
    if var1!=numeroaleatorio:
        print("Incorrecto")
        intentos+=1
    else:
        print("Numero correcto")
       

    