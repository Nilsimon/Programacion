
var1= float(input("Dime tu peso en kg:"))

var2=float(input("Dime tu estatura en metros:"))

var_estatura=var2**2

imc=var1/var_estatura

if imc>25:
    print("Si pesas", var1, "y mides",var2, ".Tu IMC es:",round(imc,2),".Hay sobrepeso")

else:
    print("Si pesas", var1, "y mides",var2, ".Tu IMC es:", round(imc))
