var1= int(input("Introduce un valor:"))

var2= int(input("Introduce otro valor:"))

if var1>10 or var2>10 or var1<1 or var2<1:
    print("uno o los dos valores estan fuera de los limites")    
else:
    if var1<var2:
        print(f"{var1} es menor a {var2}")
    
    elif var1>var2:
        print(f"{var1} es mayor a {var2}")
        
    if var1==var2:
        print("Los valores son iguales")
    
