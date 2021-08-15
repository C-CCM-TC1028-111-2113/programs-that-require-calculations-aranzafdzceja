def main():
    #escribe tu código abajo de esta línea
    entrada1 = int(input("Dame un primer número entero: "))
    entrada2 = int(input("Dame un segundo número entero: "))

    suma = entrada1 + entrada2
    resta = entrada1 - entrada2
    multiplicacion = entrada1 * entrada2

    print("Suma: " + str(suma))
    print("Resta: " + str(resta))
    print("Multiplicación: " + str(multiplicacion))

if __name__ == '__main__':
    main()
