#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice.

print("A quién madruga Dios ayuda")

frase= " A quién madruga Dios ayuda"

posicion= frase.find(input("Que palabra quieres buscar?"))
if posicion>1:
    print(f"La palabra está en la frase y está en el índice {posicion}")

else:
    print("La palabra no esta en la frase.")