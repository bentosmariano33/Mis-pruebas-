import os

# 1. Cree un script que le solicite al usuario ingresar una temperatura en grados
# Celsius, y valide que la entrada es correcta, teniendo en cuenta que la
# temperatura debe ser un valor numérico, y el rango válido está entre -18 y 50. El
# programa debe permitir reingresar el dato cuantas veces sea necesario, hasta
# que el usuario provea un dato válido. Procure informar al usuario cuando su
# dato es inválido, y cuáles son los valores aceptados.

# temperatura = int(input("Ingrese una temperatura en grados Celcius entre -18 y 50: "))
# intentos = 0

# while temperatura < -18 or temperatura > 50 and intentos < 10:
#     temperatura = int(input("El valor ingresado es incorrecto. Por favor ingrese una temperatura en grados Celcius entre -18 y 50:"))
#     intentos += 1
#     if intentos == 10:
#         print("Usted está jugando conmigo, yo me retiro.")

# 2. Cree un script que le solicite al usuario ingresar su edad. Verifique que el dato
# ingresado sea válido, teniendo en cuenta que la edad es un número entero, y el
# rango válido para este programa es de 18 a 60 años. El programa debe solicitar
# el reingreso de manera indefinida, hasta que el dato sea correcto.

# edad = int(input("Ingrese su edad. Debe ser entre 18 y 60 años."))
# intento = 0

# while edad < 18 or edad > 60 and intento < 3:
#     print("Dato incorrecto.")
#     edad = int(input("Debe ingresar una edad entre 18 y 60 años."))
#     intento += 1
#     if intento == 3:
#         print("Usted está jugando conmigo, yo me retiro.")
# print("Su edad es ",edad," .")

# 3. Modifique todos los ejercicios anteriores para que en lugar de permitir el
# reintento de manera ilimitada, el programa permita sólo 10 reintentos. Si el
# usuario supera el límite de reintentos, el programa debe terminar con el
# mensaje “Usted está jugando conmigo, yo me retiro”.

# 4. La técnica de validación para un conjunto específico de valores se puede utilizar
# para construir menús de opciones. Construya un menú que le muestre al
# usuario lo siguiente:
# ********* MI PROGRAMA *********
# 1. Saludar.
# 2. Informar temperatura.
# 3. Mostrar nombre de materia.
# 4. Salir.
# Seleccione una opción [1-4]:
# - Cuando el usuario ingrese la opción 1, se mostrará el mensaje “Hola,
# bienvenido a mi programa interactivo!”.
# - Cuando el usuario ingrese la opción 2, se mostrará el mensaje “Hay una
# sensación térmica de 20 grados Celsius.”.
# - Cuando el usuario ingrese la opción 3, se mostrará el mensaje “Estás en la
# materia Introducción a la Programación!”.
# - Cuando el usuario ingrese la opción 4, el programa debe terminar,
# mostrando el mensaje “Hasta la próxima!”.
# - Si el usuario ingresa una opción inválida, se muestra el mensaje “Opción
# inválida.”.

print("****Mi Programa****")
print("1. Saludar.")
print("2. Informar temperatura.")
print("3. Mostrar nombre de materia.")
print("4. Salir.")

opciones = int(input("Seleccione una opción [1-4]: "))

while opciones < 1 or opciones > 4:
    os.system("cls")
    print("Opción inválida")
    print("1. Saludar.")
    print("2. Informar temperatura.")
    print("3. Mostrar nombre de materia.")
    print("4. Salir.")
    opciones = int(input("Seleccione una opción [1-4]: "))
    if opciones == 1:
        print("Hola, bienvenido a mi programa interactivo!")
    elif opciones == 2:
        print("Hay una sensación térmica de 20 grados Celcius.")
    elif opciones == 3:
        print("Estas en la materia Introducción a la Programación!")
    elif opciones == 4:
        print("Hasta la próxima!")


# 5. Cree un script que le solicite al usuario ingresar cuál es su color favorito,
# limitando las opciones a rojo, verde, y azul. Aclaraciones:
# - Puede asumir que el usuario ingresará los strings en minúsculas.
# Opcionalmente, puede investigar el uso de las funciones upper() y lower()
# para transformar la entrada a mayúsculas o minúsculas y evitar así
# posibles errores de validación por este detalle.
# - Al validar entre un conjunto de opciones prefijadas (en lugar de hacerlo en
# un rango), es posible que no sea necesario validar el tipo del dato
# ingresado por teclado.
# - Al detectar un dato inválido, el programa debe darle las siguientes
# opciones al usuario:


# ** DATO INVÁLIDO **
# 1. Reintentar.
# 2. Salir.
# - La opción 1. Reintentar le permite al usuario reingresar el dato de manera
# indefinida, siempre mostrando las opciones ante cada intento fallido.
# - La opción 2. Salir finaliza el programa.

print("**Color favorito**")
print("rojo")
print("verde")
print("azul")
color = input("Ingrese su color favorito: ")
color = color.lower()
opcion = 0

while color != "rojo" and color != "verde" and color != "azul" and opcion != 2:
    os.system("cls")
    print("**DATO INVÁLIDO**")
    print("1.Reintentar.")
    print("2. Salir.")
    opcion = int(input("Seleccione una opción [1-2]: "))
    if opcion == 1:
        print("rojo")
        print("verde")
        print("azul")
        color = input("Ingrese su color favorito: ")
        color = color.lower()
    elif opcion == 2:
        print("Adios")