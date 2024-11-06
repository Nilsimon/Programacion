print("1.La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters 2.La introducció per teclat de cada caràcter respectarà la següent seqüencia i s’haurà de “forçar” els valors segons la posició indicada:")
print("Posició 1: Un numero major o igual 1 i menor o igual que 5")
print("Posició 2: Una lletra minúscula")
print("Posició 3: Una lletra majúscula")
print("Posició 4: Un dels següents símbols *, @")
print("Posició 5: Una lletra minúscula")
print("Posició 6: Un numero major o igual 6 i menor o igual que 9")
print("Posició 7: Un dels següents símbols &,/,#")
print("Posició 8: Un numero menor o igual que 5")

#Pongo un input para que el usuario introduzca el password.
password= input("Inroduce el Password siguiendo las instruciones establecidas:")

#Empiezo poniendo que si el password es menor o mayor a 8 caracteres salga error.
if len(password)>8 or len(password)<6:
    print("“Error, el password tiene una longitud de", len(password),"carácters y no cumple los requisitos”")

else:
    #Utilizamos el int para que al decir password[0]< o > a 5 o 1 no me de error.
    if int(password[0])>5 or int(password[0])<1:
        print("Error en el carácter 1")
    
    if password[1].isupper() or password.isnumeric():
        print("Error en el carácter 2")
        
    if password[2].islower() or password.isnumeric():
        print("Error en el carácter 3")
    
    if not password[3]== "*" or password[3]== "@":
        print("Error en el carácter 4")
        
    

    