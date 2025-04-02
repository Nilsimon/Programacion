milista=[]
numero=int(input("Introduce un numero"))
while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro número. Teclea 0 para salir.:"))
print(milista)
print(max(milista))
print(min(milista))