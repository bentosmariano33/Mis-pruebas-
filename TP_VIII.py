# 1. Cree un script que le pida al usuario ingresar palabras, una a una, hasta que el
# usuario ingrese la palabra “parar”. A medida que se van ingresando las
# palabras, el programa simplemente debe mostrarlas en pantalla. Al detectar la
# palabra para detenerse, debe mostrar el mensaje “--- TERMINADO ---”.

# palabra = " "
# while palabra != "parar":
#     palabra = input("Ingrese una palabra (o parar para terminar): ")
#     print(palabra)
#     if palabra == "parar":
#         print("---TERMINADO---")

# 2. Cree un script que le solicite al usuario ingresar notas de parciales por teclado,
# hasta que el usuario ingrese el valor -1, indicando que ya no hay más notas para
# cargar. Una vez ingresadas las notas, el programa debe informar la nota
# promedio (tenga cuidado de no incluir al -1 dentro del promedio).

# cantidad_notas = 0
# suma_notas = 0
# nota = int(input(f"Ingrese nota (o -1 para finalizar): "))

# while nota != -1:
#     suma_notas += nota
#     cantidad_notas += 1
#     nota = int(input("Ingrese nota (o -1 para finalizar): "))
#     if nota == -1:
#         print("No hay más notas para cargar")

if cantidad_notas > 0:        
    promedio = (suma_notas/cantidad_notas)
    print("El promedio de las notas es ",promedio)

# 3. Cree un script que le solicite al usuario leer un número entero entre 1 y 100. El
# programa debe ser capaz de solicitarle al usuario que reingrese el número
# cuantas veces sea necesario, hasta que el usuario provea un dato válido. Cada
# vez que detecte un error de validación, informele al usuario cuál fue el error, con
# los mensajes “El dato ingresado no es numérico.”, o “El número ingresado está
# fuera del rango permitido.”. Finalmente, cuando el usuario ingrese un dato
# válido, muestre el mensaje “[NÚMERO] es válido. Gracias!”.

# valor = (input("Ingrese un número entre 1 y 100: "))

# while (valor >= 1) and (valor <= 100):

# numero = (input("Ingrese un número entre 1 y 100: "))


# n = 0
# sumando = 0

# for i in range(1, n+1, 100):
#     sumando += i
# print(sumando)



# def sumaEspaciadaDel1al100(n):
#     sumando = 0
#     for i in range(1, 100+1,n+1):
#         sumando += i
#     print(sumando)

# sumaEspaciadaDel1al100(9)

c=30
for i in range(2,6):
    c = c-(i*2)
print("el resultado es:{}".format(c))