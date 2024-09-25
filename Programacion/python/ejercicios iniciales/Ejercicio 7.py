##programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedesforzar que el resultado de la división tenga 2 decimales?

var1=float(input("Dame un numero:"))

var2=float(input("Dame otro numero:"))

print("La suma es:", var1+var2)

print("La resta es:", var1-var2)

print("El producto es:", var1*var2)

print("La division es:", round(var1/var2,2))

print("El exponente es:", var1**var2)

print("La división entera es:", var1//var2)
