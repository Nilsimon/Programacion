letra= input("Introduce una letra")

if letra.isupper():
    print("La letra es mayuscula")

if letra.islower():
    print("La letra es minuscula")

elif letra.isnumeric():
    print("El valor introducido es un numero")
    
else:
    print("La letra es mayúscula ¿?")
