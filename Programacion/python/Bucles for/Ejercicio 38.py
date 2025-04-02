var_num= int(input("Dime el numero de notas:"))


for i in range(0,var_num):
        i= float(input("Dime tu nota:"))
        if i<0 or i>10:
            print("Nota equivocada")
        else: 
            if i>=5:
                print("Asignatura aprovada")  
            if i<5:
                print("Asignatura suspendida")

       
      



   