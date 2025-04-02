num= int(input("¿Cuántos numeros deseas introducir?:"))
positivos=0
negativos=0
ceros=0
for contador in range(0,num):
    contador= float(input("¿Que numeros?:"))
    if contador>0:
        positivos+=1
    elif contador<0:
        negativos+=1
    else:
        ceros+=1

print(f"Hay un total de {positivos} positivos, {negativos} negativos y {ceros} ceros.")
    

