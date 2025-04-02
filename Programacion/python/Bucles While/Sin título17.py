#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
resultado=0
repes=1

var1= int(input("introduce un numero:"))
while repes<11:
    resultado=var1*repes
    repes+=1
    print(f"{resultado}")
