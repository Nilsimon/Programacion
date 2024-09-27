#Introduce por teclado dos números y muestre por pantalla la siguiente información:
#cociente, resto y si el dividendo es par o impar

var1=float(input("Introduce un valor:"))

var2=float(input("introduce otro valor"))

var_coc=var1/var2
var_rest=var1%var2

print("El cociente es:", var_coc, "El resto es:", var_rest)

if var_rest==0:
    print("El numero es par")

else:
    print("El numero es impar")

