print("1.El password tiene que tener minimo 8 caracteres y maximo 10. 2. Posición 1: Uno de los siguientes simbolos:$€¡. Posición 2:Una letra minuscula. Posición 3: Numero entre 2 y 7. Posición 4: Letra mayuscula. Posición 5: el siguiente simbolo:>. Posición 6:Letra en minuscula. Posición 7:Un numero entre el 1-9. Posición 8: numero del 0-4. Posición 9: El simbolo @. Posición 10: Letra mayuscula")
#asigno la variable de error para sumar todos los errores posterirormente en una misma linea de codigo
err=""
#Empiezo introduciendo el for para que el usuario pueda introducir las tres contraseñas y que se recorra cada una de las posiciones posteriormente
for recorrer in range(0, 3):
    #Asigno la variable del password para luego revisar cada posición
    password= input("Introduce los passwords:")
    #Asigno esta variable para medir la longitud del password
    longitud=len(password)
    #Pongo la condición de que si los passwords son muy largos o cortos salte error
    if longitud<8 or longitud>10:
        print(f"Error, el password tiene una longitud de {longitud} caracteres y no cumple los requisitos")
    else:
        #Añado la condición de que si el password no tiene ninguno de esos simbolos en el caracter 1 salga error
        if password[0] not in "$€¡":
            err= err+("Error en el caracter 1")
            #Uso el metodo str isupper para que la posición 2 no admita mayusculas y también introduzco la variable err
        if password[1].isupper():
            err= err+("Error en el caracter 2")
        #Añado la condición en la que el password no permita un numero más pequeño a 2 o más grande a 7
        if password[2]>7 or password[2]<2:
            err=err+("Error en el caracter 3")
        #Uso el metodo str islower para que el programa no admita minusculas
        if password[3].islower():
            err=err+("Error en el caracter 4")
        #Vuelvo a utilizar el in para que si no se cumple la condicin de que ese simbolo este en el programa salte error
        if password[4] not in ">":
            err=err+("Error en el caracter 5")
        #Vuelvo a utilizar el metodo str isupper para que el programa no admita mayusculas    
        if password[5].isupper():
            err=err+("Error en el caracter 6")
        
        if password[6]>9 or password[6]<1
        
        
            
            
            
            
            
            print(err)
            
        
           
    
    