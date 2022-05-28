# from re import X


# def varios_numeros():
#     cantidad = int(input("Cuantos números quieres procesar?: "))
#     for j in range(0, cantidad):
#         numero = int(input("Ingrese un número: "))
#         if numero > 0:
#             print("Número positivo")
#         elif numero == 0:
#             print("Igual a 0")
#         else:
#             print("Número negativo")



# varios_numeros()


# def datos():
#     hay_mas_datos = "Si"
#     while hay_mas_datos == "Si":
#         x = int(input("Ingrese un número: "))
#         if x > 0:
#             print("Numero positivo")
#         elif x == 0:
#             print("Igual a 0")
#         else:
#             print("Numero negativo")
#         hay_mas_datos = input("Quiere seguir? <Si-No>: ")

# datos()

# # -------------------------------------------------------------------------------------------
# #Forma correcta de programar#
# #Ciclo interactivo#

# def pcn(x):
#     if x > 0:
#         resultado = "Número positivo"
#     elif x == 0:
#         resultado = "Igual a 0"
#     else:
#         resultado = "Número negativo"
#     return resultado

# def muchos_pcn():
#     hay_mas_datos = "Sí"
#     while hay_mas_datos == "Sí":
#         x = int(input("Ingrese un número: "))
#         print(pcn(x))
#         hay_mas_datos = input("Quiere seguir? <Sí-No>: ")

# # Test

# # def test_pcn():
# #     assert pcn(0) == "Igual a 0", "Debe ser igual a 0"
# #     assert pcn(1) == "Número positivo", "Debe ser un numero positivo"
# #     assert pcn(10) == "Número positivo", "Debe ser un numero positivo"
# #     assert pcn(-1) == "Número negativo", "Debe ser un numero negativo"
# #     assert pcn(-10) == "Número negativo", "Debe ser un numero negativo"
# #     print("Función pcn testeada exitosamente.")

# # test_pcn()


# # Ciclo con centinela

def pcn(x):
    if x > 0:
        resultado = "Número positivo"
    elif x == 0:
        resultado = "Igual a 0"
    else:
        resultado = "Número negativo"
    return resultado

def leer_centinela():
    return input("ingrese un numero (* para terminar): ")

def muchos_pcn():
    centinela = leer_centinela()
    while centinela != "*":
        x = int(centinela)
        print(pcn(x))
        centinela = leer_centinela()

muchos_pcn()

# # for i in range(100):
# #     print(i)

# # Ejercicio guiado:

# for j in range(1, 11):
#     if (j % 2) == 1:
#         print(j)
    
# cantidad = 3
# suma = 0

# for notas_prom in range(cantidad):
#     nota = input("Ingrese la nota: ")
#     suma += int(nota)
#     promedio = suma/cantidad

# print("El promedio es ", promedio)


# nota = 0
# suma_notas = 0
# alumnos = 0

# while nota >= 0: 
#    nota = int(input("Ingrese nota: "))
#    suma_notas += nota

# cantidad_notas = 0
# sumatoria = 0
# numero = int(input("Ingrese un número entero: "))

# while numero != -1:
#     sumatoria += numero
#     multiplicacion = numero * 2
#     cantidad_notas +=1
#     print(multiplicacion)
#     numero = int(input("Ingrese un número entero (si quiere terminar ingrese -1): "))

# if cantidad_notas > 0:
#     promedio = sumatoria / cantidad_notas
#     print(promedio)
# print(sumatoria)