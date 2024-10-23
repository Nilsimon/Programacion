var_nota= float(input("Dime tu nota:"))

if var_nota<0 or var_nota>10:
    print(f"La nota está fuera de los limites")
    
    
else:
    if var_nota>5:
        print(f"Tu nota es {var_nota} y has aprovado")
    elif var_nota<5:
        print(f"Tu nota es {var_nota} y has suspendido")
    