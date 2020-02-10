# Calcular si un numero es par o impar

def calcNumero ():
    print("Ingrese un numero")
    numero = int(input())

    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")



# calcNumero()
# Desarolla un programa que le pida al usuario su edad y este muetre por pantalla la etapa en la que se encuentre
# nios 5-13 aos
# Adolescentes 14-17
# Adultos jovenes 18-35
# Adultos 36-64
# tercera edad 65+

def CalcEdad():
    print("Ingrese la edad")
    edad = int(input())

    if edad >= 5 and edad <= 13:
        print("Nino")
    elif edad >= 14 and edad <= 17:
        print("Adolescente")
    elif edad >= 18 and edad <= 35:
        print("Adulto Joven")
    elif edad >= 36 and edad <= 64:
        print("Adulto")
    elif edad > 64:
        print("Tercera Edad")
    else:
        print("Fuera de Rango")

#CalcEdad()
# Escriba un programa que solicite un numero comprendido entre el 1 y el 12, con la finalidad que el programa muestre por pantalla el mes correspondiente de acuerdo al numero ingresado

def calcMes():
    print("Ingrese numero de mes")
    mes = int(input())

    if mes == 1:
        print("Enero")
    elif mes == 2:
        print("Febrero")
    elif mes == 3:
        print("Marzo")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Mayo")
    elif mes == 6:
        print("Junio")    
    elif mes == 7:
        print("Julio")    
    elif mes == 8:
        print("Agosto")    
    elif mes == 9:
        print("Septiembre")    
    elif mes == 10:
        print("Octubre")
    elif mes == 11:
        print("Noviembre")
    elif mes == 12:
        print("Diciembre")

# Los aluimnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y nombre
# El grupo A esta formado por las mujeres con un nombre anterior a la M
# El grupo B esta formado por los hombres con un nombre porterior a la N

#def CalcAlumnos():



# Escribir un programa que pregunte al usuario su nombre y sexo y este muestre por pantalla el grupo al que corresponde
def CalcGenero():
    print("Ingrese su genero")
    genero = input()
    print("Ingrese su nombre")
    nombre = input()

    print(genero)
    if genero == 'femenino':
        print("Genero:  Femenino Nombre: " + nombre)
    else:
        print("Genero:  Masculino Nombre: " + nombre)

CalcGenero()


# Escriba un programa que pida dos numeros y este le imprima por pantalla cual es el numero mayot y cual es el menor o bien que le imprima si son iguales

# Escruba un programa que pida tres numeros y que escriba:
# Si los tres osn iguales
# Si hay dos iguales
# los tres son distintos