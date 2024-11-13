print("1.La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters 2.La introducció per teclat de cada caràcter respectarà la següent seqüencia i s’haurà de “forçar” els valors segons la posició indicada:")
print("Posició 1: Un numero major o igual 1 i menor o igual que 5")
print("Posició 2: Una lletra minúscula")
print("Posició 3: Una lletra majúscula")
print("Posició 4: Un dels següents símbols *, @")
print("Posició 5: Una lletra minúscula")
print("Posició 6: Un numero major o igual 6 i menor o igual que 9")
print("Posició 7: Un dels següents símbols &,/,#")
print("Posició 8: Un numero menor o igual que 5")

#asigno la variable de error para sumar todos los errores posterirormente en una misma linea de codigo
err=""
#Pongo un input para que el usuario introduzca el password.
password= input("Inroduce el Password siguiendo las instruciones establecidas:")

#Empiezo poniendo que si el password es menor o mayor a 8 caracteres salga error.
if len(password)>8 or len(password)<6:
    print("“Error, el password tiene una longitud de", len(password),"carácters y no cumple los requisitos”")

else:
    #Utilizamos el int para que al decir password[0]< o > a 5 o 1 no me de error.
    if int(password[0])>5 or int(password[0])<1:
       err= err+("Error en el caracter 1 ")
        
    #Isupper o isnumeric para que la contraseña no admita ni simbolos ni letras mayusculas
    if password[1].isupper() or password[1].isnumeric():
        err=err+("Error en el caracter 2 ")
    #Lo mismo de antes pero que el programa no admita minusculas simbolos ni numeros  
    if password[2].islower() or password[2].isnumeric():
        err=err+("Error en el caracter 3 ")
    
    #uso el not in para que si no se cumple la condición de que no so ninguno de esos simbolos printee error
    if password[3] not in "@*_":
        err=err+("Error en el caracter 4 ")
        
    if password[4].isupper():
        err=err+("Error en el caracter 5 ")
    
    if int(password[5])>9 or int(password[5])<6:
        err=err+("Error en el caracter 6 ")
        
    if password[6] not in "%/#":
        err=err+("Error en el caracter 7 ")
        
    if int(password[7])>5:
        err=err+("Error en el caracter 8 ")
    
    else:
        print("El formato del password es válido ")
        
print(err)
   


    