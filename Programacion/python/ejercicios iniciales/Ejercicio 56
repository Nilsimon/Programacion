#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
print("""MENÚ
1. Bocadillo de calamares- 9 €"
2. Bocadillo de chistorra - 4.5 €
3. Bikini de jamón - 2.5 €"
ACOMPAÑAMIENTO
1. Patatas finas - 1.5 €
2. Patatas gruesas - 1.75 €
3. Patatas rústicas - 2 €
BEBIDAS
1. Coca cola - 2 €"
2. Acuarius - 1.5 €
3. Agua - 1 €""")
repes=0
menu=0
menu2=0
menu3=0
bebida=0
bebida2=0
bebida3=0
acomp=0
acomp2=0
acomp3=0
total=0
seguir=0
descuento=0
IVA=0.1
while seguir!= "n":
    varmenu= int(input("Introduzca el numero de bocadillo deseado:"))
    varacomp= int(input("Introduzca el numero de acompañamiento deseado:"))
    varbebidas= int(input("Introduzca el numero de bebida deseado:"))
    if varmenu==1:
        menu=9
    elif varmenu==2:
        menu2= 4.5
    elif varmenu==3:
        menu3= 2.5
    if varacomp==1:
        acomp= 1.5
    elif varacomp==2:
        acomp2= 1.75
    elif varacomp==3:
        acomp3= 2
    if varbebidas==1:
        bebida= 2
    elif varbebidas==2:
        bebida2= 1.5
    elif varbebidas==3:
        bebida3= 1
    total= menu+menu2+menu3+bebida+bebida2+bebida3+acomp+acomp2+acomp3
    seguir= input("Desea volver a pedir?:")
    repes+=1
    if total>20 and total<30:
        descuento= total-(total*0.5)
    if total>30:
        descuento= total-(total*0.5)
    IVA=total+(total*IVA)
print(f"El total a pagar es: {total}  . Con IVA el total es {IVA}. Con su descuento aplicado {descuento}. Numero de pedidios {repes}")
        
         
         
     
    
        
