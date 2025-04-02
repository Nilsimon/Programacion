#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

var_num= int(input("Dime un numero:"))

suma= 0

for resultado in range(0, var_num + 1):
    suma= suma+resultado
print(f"La suma de los primeros {var_num} naturales es {suma}")

