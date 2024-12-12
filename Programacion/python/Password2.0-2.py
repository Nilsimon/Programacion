print("1.La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters 2.La introducció per teclat de cada caràcter:")
print("3 numeros:  Un numero major o igual 1 i menor o igual que 5;  Un numero major o igual 6 i menor o igual que 9; Un numero menor o igual que 5 ")
print("Tres letras: 1 Minúscula y 2 Mayusculas")
print("2 Simbolos:  Un dels següents símbols *, @; Un dels següents símbols &,/,#")
#Creo una variable correcto para contar cada password que está bien
correcto=0
#Creo una variable error para después contar los errores por password
err=0
#Asigno las vaariables de mayuscula y minuscula, numero y simbolo.
mayus=0
minus=0
numero_1=0
numero_2=0
numero_3=0
simbolo_1=0
simbolo_2=0
#Empiezo introduciendo el for para que el usuario pueda introducir las tres contraseñas y que recorra el password para ver si se cumplen las condiciones
for recorrer in range(3):
    #Asigno la variable del password para luego revisar cada posición
        password= input("Introduce los passwords:")
    #Asigno esta variable para medir la longitud del password
        longitud=len(password)
    #Pongo la condición de que si los passwords son muy largos o cortos salte error y sumamos a la variable err +1 para printear el posible error más adelante
        if longitud<6 or longitud>8:
            print(f"Error, el password tiene una longitud de {longitud} caracteres y no cumple los requisitos")
            err+=1

        #Pongo este for para que en este caso la variable "i" recorra el password y que el programa recorra todos los caracteres para ver si el numero de estos es valido y también si los caracteres son validos
        for i in password:
            #Uso el metodo str islower() para que si el usuario introduce minusculas se sume uno a la ar minus
             if  i.islower():
                minus+=1
            #Para ver las demás condiciones uso el elif y también el metodo str isupper() para que si el usuario introduce minusculas se sume uno a la var mayus
             elif i.isupper():
                 mayus+=1
            #Uso el in para que si el numero esta dentro de las comillas se sume un +1 a la variable
             elif i in "12345":
                 numero_1+=1
            #Hago lo mismo en esta linea de codigo
             elif i in "6789":
                 numero_2+=1 
            #Otra vez uso el in
             elif i in "012345":
                numero_3+=1
             elif i in "*@":
                simbolo_1+=1
             elif i in "&/#":
                simbolo_2+=1
#Verifico si todas las condiciones se cumplen mediante añadiendo la suma total de cada franja de variables(letras, numeros, simbolos)
        tot_num= numero_1 + numero_2 + numero_3 
        tot_simb= simbolo_1 + simbolo_2
#Si los passwords son correctos a cada vuelta el codigo añadirá un +1 a la variable correcto
        if mayus==2 and minus==1 and tot_num==3 and tot_simb==2:
                correcto+=1
#Si no se cumplen ninguna de las siguientes condiciones hago que se añada a error +1
        else:
                err+=1
#Printeo el numero de passwords erroneos y  correctos
print(f"De los tres passwords introducidos, {err} password/s son erroneos y {correcto} son correcto/s")


    
            
                
            
                
            
            
   
        
        
            
            
            
            
          
            
        
           
    
    
