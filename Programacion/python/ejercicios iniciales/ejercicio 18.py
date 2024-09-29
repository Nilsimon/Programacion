
var1=int(input("¿Cuantos años tiene?:"))

if var1<18:
    var2=int(input("Cuantas entradas quieres?:"))

    var3=0,5*(var2*12)

    var4=var2*12

    total= (var4-var3)

    print("El precio total del cine para el menor/es es:", var4)

else:
    var2=int(input("Cuantas entradas quieres?:"))
    var3=0,5*(var2*12)
    var4=var2*12
    var5= (var4-var3)
    print("El precio total del cine para el adulto/s es:", var5)
 
    
    


    
    



