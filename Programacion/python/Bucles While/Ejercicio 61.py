#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
resultado=0
repes=1

var1= int(input("introduce un numero:"))
while repes<11 and resultado<40:
    resultado=var1*repes
    repes+=1
    print(f"{resultado}")
print("Programa finalizado")
