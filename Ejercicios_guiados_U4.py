#Codifique un programa que solicite al usuario ingresar dos números enteros, 
# y luego informe si la suma de ambos es mayor a 100 o no.

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

if num1 + num2 > 100:
    print("La suma de ambos números es mayor a 100.")
else:
    print("La suma de ambos números es menor a 100.")

#Agregue una función que reciba dos enteros como parámetro, 
#e informe (mostrando en pantalla) si al menos uno de los valores es mayor a 50.

def mayor_a_50(a,b):
    """
    INPUT: a, b (int)
    OUTPUT: "Al menos uno de los valores es mayor a 50." (string)
    "mayor" es la variable para el output.
    """
    if a or b > 50:
        mayor = "Al menos uno de los números es mayor a 50."
        return mayor

print(mayor_a_50(num1,num2))

#Agregue una función que reciba dos enteros como parámetro, 
#e informe (mostrando en pantalla) si ambos valores son menores que 100.

def menor_a_100(a,b):
    """
    INPUT: a, b (int)
    OUTPUT: "Ambos valores son menores que 100"
    """
    if a < 100 and a < 100:
        menores = "Ambos valores son menores que 100"
        return menores
    elif a or b > 100:
        mayor_a_100 = "Al menos un valor es mayor a 100"
        return mayor_a_100

print(menor_a_100(num1,num2))