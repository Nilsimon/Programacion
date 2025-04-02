#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con Whil
repe=0
while repe!="n":
    var1=int(input("Introduce un numero: "))
    var2=int(input("Introduce otro numero: "))
    print(var1+var2)
    repe=input("Desea repetir?: ")
print("Programa finalizado")

