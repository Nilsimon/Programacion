import math
a= float(input("Dime un valor:"))
b=float(input("Dime otro valor:"))
c=float(input("Dime otro valor:"))

var_dentro= b**2-4*a*c
var_raiz= math.sqrt(var_dentro)
var_resultado1= (-b+var_raiz)/2*a
var_resultado2= (-b-var_raiz)/2*a
if var_dentro<0:
   print:("La raiz no puede ser negativa")

else:
    print("El resultado de X1=", round(var_resultado1,2), "i X2=", round(var_resultado2,2))



