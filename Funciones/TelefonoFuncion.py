# Se requiere relizar un programa que facture el uso de un telefono considerando lo siguiente:
# a. Le pedira la captura la tarifa por segundo al usuario
# b. Solicita al usuario la cantidad de comunicaciones que se realizaron
# c. Solicitara al usuario la duracion de cada comunicacion, expresada en horas, minutos y segundos
# d. Imprime el valor de la llamada  la cantidad de comunicaciones
# e. Imprime la cantidad total acumulada en funcion a las llamadas realizadas.

def ConvertirSegundos(Horas, Minutos, Segundos):
    # convertir horas
    segHoras =  Horas * 3600

    # convertir Minutos
    segMinutos = Minutos * 60
    # Juntar todos los segundos:
    return segHoras + segMinutos + Segundos

    
total = 0
tarifaSegundo = int(input('Ingrese la tarifa por segundo: '))
cantLlamadas =  int(input('Ingrese el numero de llamadas realizadas: '))

for x in range(cantLlamadas):
    horas = int(input('Ingrese las horas de la llamada ' + str(x + 1)))
    minutos = int(input('Ingrese los minutos de la llamda ' + str(x + 1)))
    segundos = int(input('Ingrese los segundos de la llamada ' + str(x +1)))
    print('Valor de la llamada ', x + 1 , ': ' , ConvertirSegundos(horas, minutos, segundos) * tarifaSegundo)
    total += ConvertirSegundos(horas, minutos, segundos) * tarifaSegundo
print('Total acumulado ', total, 'Numero de llamadas realizadas: ', cantLlamadas)


