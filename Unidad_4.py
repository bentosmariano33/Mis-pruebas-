def positivo(x):
    if x>0:
        print("El número es positivo")
    if not x>0:
        print("El número es negativo")

x = int(input("Ingrese un número: "))
positivo(x)



sueldo_basico = 800

if seccion == 1:
    sueldo = sueldo_basico + 120
    if antiguedad < 5:
        sueldo = sueldo + (sueldo * 10) / 100
    else:
        sueldo = sueldo + (sueldo * 20) / 100
else:
    sueldo = sueldo_basico + 250
