# 1.
# Escriba en un programa que solicite un valor numerico al usuario y que compruebe si el valor
#  ingresado es menor que el numero 10, en caso de ser menor el valor ingresado debe volver a 
# solicitar el valor numerico repitiendo el ciclo hasta que el usuario ingrese el valor mayor  
#  que 10, finalmente debe escribir por pantalla los dos valores ingresados cuando se cumpla con la 
# condicion
def numeroMayor():
    numero = int(input('Ingrese un numero'))
    while (numero <= 10):
        numero = int(input('numero menor o igual que 10, Ingrese otro numero'))
    print('El numero ' + str(numero) + ' si es mayor que 10')

#numeroMayor()

# 2. Escriba un programa que solicite un valor numerico al suiuario y que comprieba si el valor
#  ingresado se encuentra en un rango de 10 a 20, el programa finaliza cuando el usuario ingresa
#  un valor que esta dentro del rango
def ejercicio2():
    numero = int(input('Ingrese un numero'))
    
    while (numero < 10 or numero > 20):
        
        numero = int(input('numero fuera de rango, ingrese un numero del 10 al 20'))
    print('El numero: ' + str(numero) + ' esta en rango')

#ejercicio2()





# 3. Escruba un programa quw pida dos numeros el programa pedira de nuevo el segundo numero muentras
#  este no sea mayoy que el primero, el programa finalizara cando el segundo numero sea mayor que el
#  primero, el programa finalizara cuando el numero sea mayor que el primero capturado y escribiendo
#  los dos numeros

#def ejercicio3():


# 4. Escribe un programa que pida un numero, el programa pedira de nuevo el mundo, si es que este no
#  cae en el rango del 0 al 20, una vez que e usuario ingrese un valor comprendido en el rango el 
# programa finaliza y le muestra por pantalla la cantidad de intentos realizados.

# def ejercicio4():
#     numero = int(input("Ingresa un numero "))



# 5. escriba un programa que pida un numero, el programa calculara el cuadrado desde el numero 1
#  hasta el valor intruducido por el usuario, los resultados los imprime por ptantallla utilizando un formato tabulador horizoantal

def ejercicio5():
    valor = input("Escriba un valor:")
    intentos = 1
    while int(valor) < 10 or int(valor) > 20:
        valor = input("Escriba un valor: ")
        intentos += 1
        continue
    print(intentos, " intentos")
# 6. Escribe un programa que pida un numero el programa pedira de nuevo un numero si es que este no 
# cae en el rango del 0 al 20 el programa solo debe permitir 10 intentos, una vez que el usuario 
# ingrese un valor comprendido en el rango del programa finaliza y le muestra por pantalla la 
# cantidada de intentos realizados.
def ejercicio6():
    valor = input("Escriba un valor:")
    intentos = 1
    while int(valor) < 10 or int(valor) > 20:
        valor = input("Escriba un valor: ")
        intentos += 1
        if intentos == 10:
            print(intentos, " intentos")
            break
        continue
    
ejercicio6()