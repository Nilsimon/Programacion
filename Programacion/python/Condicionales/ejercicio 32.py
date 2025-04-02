
print("A quién madruga Dios ayuda")

frase= " A quién madruga Dios ayuda"

posicion= frase.find(input("Que palabra quieres buscar?"))
if posicion>0:
    print(f"La palabra está en la frase y está en el índice {posicion}")

elif posicion<0:
    posicion.capitalize()
    print(f"La palabra está en la frase y está en el índice {posicion}")

