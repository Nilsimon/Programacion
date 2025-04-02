#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
repe=0
repes=0
while repe!="n":
    var1=int(input("Introduce un numero: "))
    var2=int(input("Introduce otro numero: "))
    suma= var1+var2
    print(suma)
    repe=input("Desea repetir?: ")
    repes+1
print("Programa finalizado")
