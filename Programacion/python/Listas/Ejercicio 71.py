#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
letras = []
continuar = "s"
while continuar != "n":
    letra = input("Introduce una letra: ").lower()
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, introduce solo una letra.")
    elif letra not in letras:
        letras.append(letra)
    else:
        print("Letra repetida, no se agrega.")
    continuar = input("¿Quieres seguir introduciendo letras? (s/n): ").lower()

print("Letras guardadas (sin repetir):")
for l in letras:
    print(l)
