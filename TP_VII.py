# 1. Cree un script para mostrar los primeros 100 números enteros positivos, comenzando desde el 1.

from functools import total_ordering


# for ent_positivos in range(1, 101):
#     print(ent_positivos)

# # 2. Modifique el script del ejercicio anterior para que se muestren sólo los números pares. Para saber si un número es par, utilice el operador de módulo (%).

# for ent_positivos in range(1, 101):
#     if (ent_positivos % 2 == 0):
#         print(ent_positivos)

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





