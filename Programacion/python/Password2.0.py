print("1.La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters 2.La introducció per teclat de cada caràcter:")
print("3 numeros:  Un numero major o igual 1 i menor o igual que 5;  Un numero major o igual 6 i menor o igual que 9; Un numero menor o igual que 5 ")
print("Tres letras: 1 Minúscula y 2 Mayusculas")
print("2 Simbolos:  Un dels següents símbols *, @; Un dels següents símbols &,/,#")
#Creo una variable correcto para contar cada password que está bien
correcto=0
#Creo una variable error para después contar los errores por password
err=0
#Asigno las vaariables de mayuscula y minuscula, numero y simbolo también asigno una variable chivato para  no tener que comprobar si las condiciones se cumplen o no.
mayus=0
minus=0
numero=0
simbolo=0
inc= False
#Pongo una variable contador para que se incremente a cada vuelta y así no me salte error al recorrer el password
contador=0
#Empiezo introduciendo el for para que el usuario pueda introducir las tres contraseñas y que recorra el password para ver si se cumplen las condiciones
for recorrer in range(0, 3):
    #Asigno la variable del password para luego revisar cada posición
    password= input("Introduce los passwords:")
    #Asigno esta variable para medir la longitud del password
    longitud=len(password)
    #Pongo la condición de que si los passwords son muy largos o cortos salte error
    if longitud<6 or longitud>8:
        print(f"Error, el password tiene una longitud de {longitud} caracteres y no cumple los requisitos")
    inc= True
    
    else:
        #Pongo este for para que en este caso la variable "i" recorra el password.
        for i in password:
            #Miramos la condición de las letras y si hay mayuscula se suma 1 a la variable y si no se queda en 0 lo mismo con las minusculas
            if  i.islower() or i.isupper():
                mayus+=1
                minus+=1
                inc=True
                
            #Uso el is in para que si se cumple que en el password estan dos de esos simbolos se añada que en la variable de simbolos hay dos simbolos
            if i is in " *@&/#":
                simbolo+=1
                inc=True
            #Vuelvo a usar el is in para que si se cumple que en el password estan tres de esos numeros cerrados con comillas se añada uno al contador de numeros
            if i is in "12345" or i is in "6789" or i is in "012345":
                numero+=1
                inc=True
            #
            if mayus==2 and minus==1 and numero==3 and simbolo==2:
                correcto+=1
           #Si no se cumplen ninguna de las siguientes condiciones hago que se añada a error +1
            else:
                err+=1
if mayus==2 and minus==1 and numero==3 and simbolo==2:
    
    
    
    

print(f"De los tres passwords introducidos, {err} passwords son erroneos y ")


    
            
                
            
                
            
            
   
        
        
            
            
            
            
          
            
        
           
    
    