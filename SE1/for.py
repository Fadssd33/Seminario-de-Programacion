def main():
    entrada = input('Escribe una frase:')
    contador = 0
    cuentaletra = input('Captura la letra a evaluar:')

    for letra in entrada:
        if letra == cuentaletra:
            print((cuentaletra), (contador))
            contador += 1

main()

