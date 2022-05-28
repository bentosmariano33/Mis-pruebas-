# 1. Cree un script que le solicite al usuario ingresar una temperatura en grados
# Celsius, y valide que la entrada es correcta, teniendo en cuenta que la
# temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El
# programa debe permitir reingresar el dato cuantas veces sea necesario, hasta
# que el usuario provea un dato válido. Procure informar al usuario cuando su
# dato es inválido, y cuáles son los valores aceptados.

temperatura = int(input("Ingrese una temperatura en grados Celcius entre -18 y 50: "))

while temperatura < -18 or temperatura > 50:
    temperatura = int(input("El valor ingresado es incorrecto. Por favor ingrese una temperatura en grados Celcius entre -18 y 50:"))