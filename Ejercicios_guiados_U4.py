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
    OUTPUT: None
    Muestra por pantalla si a o b es mayor a 50
    """
    if a > 50 or b > 50:
        print("Al menos uno de los números es mayor a 50.")

mayor_a_50(num1,num2)

    #Agregue una función que reciba dos enteros como parámetro, 
#e informe (mostrando en pantalla) si ambos valores son menores que 100.

def menor_a_100(a,b):
    """
    INPUT: a, b (int)
    OUTPUT: None
    "Ambos valores son menores que 100"
    """
    if a < 100 and b < 100:
        print("Ambos valores son menores que 100")

menor_a_100(num1,num2)
    