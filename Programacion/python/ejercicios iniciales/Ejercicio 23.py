var_nota= float(input("Dime tu nota:"))

if var_nota<0 or var_nota>10:
    print(f"La nota está fuera de los limites")
    
else:
    if var_nota<5:
        print(f"Tu nota es {var_nota}, has sacado insuficiente")
    elif var_nota>5 and var_nota<6.5:
        print(f"Tu nota es {var_nota}, has sacado suficiente")
    elif var_nota>6.5 and var_nota<8.5:
        print(f"Tu nota es {var_nota}, has sacado notable")
    elif var_nota>8.5:
        print(f"Tu nota es {var_nota}, has sacado excelente")
    
    


