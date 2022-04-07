# 1. Cree una función que reciba dos números como parámetro, y 
# muestre en pantalla la suma aritmética de ambos. 
# Invoque a la función con dos números leídos desde teclado.

def suma(num1,num2):
    """
    INPUT: num1 y num2 (int)
    OUTPUT: sumados (num1+num2)
    "La variable donde se suman num1 y num2 se llama sumados"
    """
    sumados = num1+num2
    print(sumados)

suma(1,5)

def testsuma(num1,num2):
    print("Validando la función suma()...")
    assert suma(4,5) == 9
    assert suma(-2,5) == 3
    assert suma(2,-3)

