#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while

var1=int(input("introduce un numero:"))
var2=int(input("introduce otro numero:"))
var3=0
concatenarpar=""
concatenarimp=""
if var1>var2:
    var3=var1
    var2=var3
    var1=var2
for recorrer in range(var1,var2):
    if recorrer%2==0:
        print(recorrer, "es par")
    else:
        print(recorrer, "es impar")
    