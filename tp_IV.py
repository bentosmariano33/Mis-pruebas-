#1. Cree una función que reciba dos números como parámetro, y muestre en pantalla la suma aritmética 
# de ambos. Invoque a la función con dos números leídos desde teclado. 

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

def suma(a, b):
    resultado = a+b
    print(resultado)

suma(num1,num2)
        