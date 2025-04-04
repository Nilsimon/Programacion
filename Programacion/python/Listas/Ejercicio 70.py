#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
palabras=[]
palabras2=[]
repes=int(input("Cuantas palabras quieres poner?: "))
for palabras_ in range(repes):
    palabras2= palabras_= input()
palabras=palabras_.split()
palabras.reverse()
v=" ".join(palabras)
print(palabras2)
print(v)
