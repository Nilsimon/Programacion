var1=float(input("Introduce el peso: "))
var2=float(input("Introduce la altura: "))
var_imc= var1/var2**2
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es:", round(var_imc,2)
if 25<var_imc:
 print("Hay sobrepeso")
else:
 print("Estás dentro de los parámetros normales")

