# 1. Cree un script para mostrar los primeros 100 números enteros positivos, comenzando desde el 1.

# primeros_enteros = 10
# for ent_positivos in range(1, primeros_enteros + 1):
#     print(ent_positivos)

# # 2. Modifique el script del ejercicio anterior para que se muestren sólo los números pares. Para saber si un número es par, utilice el operador de módulo (%).


# for ent_positivos in range(1, primeros_enteros + 1):
#     if (ent_positivos % 2 == 0): #calcula el módulo del valor
#         print(ent_positivos)

# 3. Cree un script para calcular el resultado de sumar los números desde el 75 al 150.

def sumar_num(x, y):
    total = 0
    for j in range(x, y+1):
         total += j
    return total

print(sumar_num(1, 99))

# valor_x = 150
# total_2 = 0

# for i in range(75, valor_x + 1):
#     total_2 += i

# print(total_2)

# 4. Cree un script que le solicite al usuario ingresar un número entero, y muestre en pantalla el factorial de dicho número. 
# NOTA: puede obviar la validación en este ejercicio, pero recuerde que la función range no incluye al valor máximo enviado como parámetro. 
# factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n

# numero_usuario = int(input("Ingrese un número: "))
# factorial = 1

# for fact in range(numero_usuario):
#     if numero_usuario > 0:
#         print(factorial * numero_usuario * (numero_usuario - 1))

# 5. Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, informarle si el mismo es positivo, negativo, o cero.

# cantidad_de_num = 1

# for valor_num in range(cantidad_de_num):
#     numero = int(input("Ingrese un número: "))
#     if numero > 0:
#         print("Positivo")
#     elif numero == 0:
#         print("Cero")
#     else:
#         print("Negativo")

# 6. Cree un script que le solicite al usuario ingresar 10 números, y una vez
# ingresados, le muestre en pantalla cuál es el máximo, y en qué posición lo
# ingresó. Por ejemplo, si el usuario ingresa los números 2, 63, -3, 20, 55, 89, 7, 32, 9,
# y 33, se le debería mostrar el mensaje “El mayor número ingresado es 89, y lo
# ingresaste en la posición 6”. NOTA: las posiciones posibles comienzan desde 1.

num_usuario = 3
num_mayor = -999999
num_menor = 999999

# for number in range(1, num_usuario + 1):
#     num = int(input("Ingrese un número: "))
#     if num > num_mayor:
#         num_mayor = num
#         posicion_num_mayor = number

# print("El mayor número ingresado es ", num_mayor, "y lo ingresaste en la posición ", posicion_num_mayor)

# 7. Extienda el script del ejercicio anterior para que también informe el número
# mínimo ingresado, y su posición.

for number in range(1, num_usuario + 1):
    num = int(input("Ingrese un número: "))
    if num > num_mayor:
        num_mayor = num
        posicion_num_mayor = number
    elif num < num_menor:
        num_menor = num
        posicion_menor = number

print("El mayor número ingresado es ", num_mayor, "y lo ingresaste en la posición ", posicion_num_mayor)
print("El número mínimo ingresado es ", num_menor, "y su posición es ", posicion_menor)



# 8. Un cliente ha solicitado un programa que le permita ingresar los mililitros de
# lluvia caídos diariamente en una semana, para que el programa le informe en
# pantalla el promedio de precipitación de esa semana. El cliente también desea
# saber cuál fue el día en que más llovió en la semana.
# A modo ilustrativo, un reporte generado por el programa debería verse como
# sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
# El promedio de precipitaciones fue de XX mls. diarios.
# El día de más precipitaciones fue el xxxxxx (nombre del día).
# Tenga en cuenta que la numeración de los días de la semana comienza con el 1
# para el día domingo.
# Codifique el programa para dar solución a lo solicitado por el cliente.

# mililitros_caidos = 0
# cantidad_de_dias = 7
# dia_mas_lluvioso = 0

# for dia in range(1, cantidad_de_dias + 1):
#     lluvia = int(input("Ingrese los mililitros caidos: "))
#     mililitros_caidos += lluvia

#     if dia_mas_lluvioso < lluvia:
#         dia_mas_lluvioso = lluvia
#         dia_max_lluvia = dia

#     if dia_max_lluvia == 1:
#         print("Domingo")
#     elif dia_max_lluvia == 2:
#         print("Lunes")
#     elif dia_max_lluvia == 3:
#         print("Martes")
#     elif dia_max_lluvia == 4:
#         print("Miércoles")
#     elif dia_max_lluvia == 5:
#         print("Jueves")
#     elif dia_max_lluvia == 6:
#         print("Viernes")
#     else:
#         print("Sábado")

# promedio_precipitaciones = mililitros_caidos / cantidad_de_dias
# print("El promedio de precipitaciones fue de ", promedio_precipitaciones, " mls. diarios.")
# print("El día de más precipitaciones fue el ", dia_max_lluvia)






