def positivo(x):
    if x>0:
        print("El número es positivo")
    if not x>0:
        print("El número es negativo")

x = int(input("Ingrese un número: "))
positivo(x)