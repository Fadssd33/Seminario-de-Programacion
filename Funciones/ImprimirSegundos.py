# Define una funcion llamada ImprimirSegundos(Horas,Minutos, Segundos)
# que imprima por pantalla la conversion a segundos
#  una medida de tiempo, expresada en horas, munutos
#  y segundos

def ImprimirSegundos(Horas, Minutos, Segundos):
    # convertir horas
    segHoras =  Horas * 3600

    # convertir Minutos
    segMinutos = Minutos * 60
    # Juntar todos los segundos:
    total = segHoras + segMinutos + Segundos
    print('Segundos totales ', total)


horas = int(input('Ingrese las horas: '))
minutos = int(input('Ingrese los minutos: '))
segundos = int(input('Ingrese los segundos: '))

ImprimirSegundos(horas, minutos, segundos)