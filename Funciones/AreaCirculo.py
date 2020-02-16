import math
# Realiza una funcion llama AreaCirculo(Radio),
#  que devuelva el area de un circulo a partir de 
# un radio

def AreaCirculo(Radio):
    area =  math.pi * (Radio**2)
    #print('El area del circulo es: ' + str(area))
    print('area:', area)


radio = int(input("Ingrese un radio: "))
AreaCirculo(radio)