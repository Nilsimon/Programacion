#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif.

var_frase= input("Introduce una frase:")

if len(var_frase)<11:
    print("la longitud es menor a 11 caracteres")
    
elif len(var_frase)>11:
    print("la frase tiene mas de 11 caracteres")

print("longitud es", len(var_frase) )


