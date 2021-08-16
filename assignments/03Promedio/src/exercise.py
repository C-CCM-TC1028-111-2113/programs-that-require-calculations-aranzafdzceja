def main():
    #escribe tu código abajo de esta línea
    calif1 = float(input("Dame la calificación de tu primer materia: "))
    calif2 = float(input("Dame la calificación de tu segunda materia: "))
    calif3 = float(input("Dame la calificación de tu tercera materia: "))
    calif4 = float(input("Dame la calificación de tu cuarta materia: "))
    
    prom = calif1 + calif2 + calif3 + calif4 
    prom = prom / 4
    
    print("El promedio es: " + str(prom))

if __name__ == '__main__':
    main()
