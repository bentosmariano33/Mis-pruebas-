# 1. Cree un script para mostrar los primeros 100 números enteros positivos, comenzando desde el 1.

primeros_enteros = 1
for ent_positivos in range(1, primeros_enteros + 1):
    print(ent_positivos)

# # 2. Modifique el script del ejercicio anterior para que se muestren sólo los números pares. Para saber si un número es par, utilice el operador de módulo (%).


for ent_positivos in range(1, primeros_enteros + 1):
    if (ent_positivos % 2 == 0):
        print(ent_positivos)

# 3. Cree un script para calcular el resultado de sumar los números desde el 75 al 150.

def sumar_num(x, y):
    total = 0
    for j in range(x, y+1):
         total += j
    return total

print(sumar_num(1, 3))

# 4. Cree un script que le solicite al usuario ingresar un número entero, y muestre en pantalla el factorial de dicho número. 
# NOTA: puede obviar la validación en este ejercicio, pero recuerde que la función range no incluye al valor máximo enviado como parámetro. 
# factorial de n = n! = 1 * 2 * 3 * … * (n - 1) * n

# 5. Cree un script que le solicite al usuario ingresar 10 números enteros, y por cada uno, informarle si el mismo es positivo, negativo, o cero.

cantidad_de_num = 10

for valor_num in range(cantidad_de_num):
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        print("Positivo")
    elif numero == 0:
        print("Cero")
    else:
        print("Negativo")


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

# for dia in range(cantidad_de_dias):
#     lluvia = int(input("Ingrese los mililitros caidos: "))
#     mililitros_caidos += lluvia

# promedio_precipitaciones = mililitros_caidos / cantidad_de_dias
# print("El promedio de precipitaciones fue de ", promedio_precipitaciones, " mls. diarios.")






