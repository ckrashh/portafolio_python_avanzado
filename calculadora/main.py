from calculadora import calculadora
if __name__ == "__main__":
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            calculo = calculadora(a, b)
            print("Suma:", int(calculo.sumar()))
            print("Resta:", int(calculo.restar()))
            print("Multiplicación:", round(calculo.multiplicar(), 2))
            print("División:", round(calculo.dividir(), 2))
        except ValueError:
            print("Por favor, ingrese solo números.")