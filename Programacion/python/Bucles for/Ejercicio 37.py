
var_num= int(input("Dime el numero de notas:"))


for i in range(0,var_num):
        i= float(input("Dime tu nota:"))
        if i<5:
            print("Asignatura suspendida")
else:
    print("Asignatura aprovada")        
