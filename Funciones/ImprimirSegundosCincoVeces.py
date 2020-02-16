# Define una funcion llamada ImprimirSegundos(Horas, Minutos, Segundos), que imprima por pantalla la conversion
#  a segundos una medida de tiempo expresada en horas, minutos y segundos
# El programa debe solicitarle cinco veces la cantidad en Horas, minutos y segundos
# Imprime por pantalla la cantidad de veces que el programa solicito los datos
def ImprimirSegundos(Horas, Minutos, Segundos, NumSolicitud):
    # convertir horas
    segHoras =  Horas * 3600

    # convertir Minutos
    segMinutos = Minutos * 60
    # Juntar todos los segundos:
    total = segHoras + segMinutos + Segundos
    print('Segundos totales ', total, 'Solicitud numero: ', NumSolicitud)

for x in range(5):
    horas = int(input('Ingrese las horas: '))
    minutos = int(input('Ingrese los minutos: '))
    segundos = int(input('Ingrese los segundos: '))
    numSolicitud =  x + 1
    ImprimirSegundos(horas, minutos, segundos, numSolicitud)
