# Realiza un programa el cual contenga un universo
#  de 12 valores y que imprimir por pantalla los numeros impares

def NumImpares():
    x = range(12)
    for n in x:
        if (n%2 != 0):
            print(n)
#NumImpares()
#Escribe un programa que le pida la edad al usuario por pantalla y este imprima los años que ha
# cumplido desde 1 hasta su edad, para la realizacion de este programa utiliza el tipo de datos range
def edad():
    edad = input('Ingrese Edad')
    for x in range edad:
        
# Escriba un programa que imprima a tabla de multiplicar del 5
def TablaCinco():
    x = range (10)
    for n in x:
        print((n + 1)* 5)
#TablaCinco()

# Escriba un programa que muestre por pantalla la tabla de multiplicar
# del 1 al 10
# Utiliza el tipo de datos range
# Utiliza el argunmento end it con la finalidad que el print 
def TablaDiez():
    for x in range(10):
        for y in range(10):
            print((x + 1) * (y + 1))
TablaDiez()
# Escribe un programa que solicite una frase y este regrese por pantalla 
# la impresion de cada una de las letras que contiene la frase
def ImprimirCaracteres():
    word = input('Ingrese una palabra')
    for char in word:
        print(char)

#ImprimirCaracteres()