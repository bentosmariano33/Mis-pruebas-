#1. Cree una función que reciba dos números como parámetro, y muestre en pantalla la suma aritmética 
# de ambos. Invoque a la función con dos números leídos desde teclado.
# #2. Modifique el script del ejercicio anterior para que la función retorne el resultado en vez de mostrarlo. 
#El programa debe seguir mostrando el resultado en pantalla. 

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

def suma(a, b):
    resultado = a+b
    return resultado

print(suma(num1,num2)) #con esta función se muestra el resultado en pantalla luego de retornarlo.

# 3. Cree una función que reciba un string como parámetro, y retorne la cantidad de letras que posee. 
# Luego, utilice la función para escribir un programa que solicite ingresar el nombre del usuario, 
# y luego muestre en pantalla cuántas letras tiene ese nombre.

def palabra(p):
    cont_letras = len(p)
    return cont_letras

tu_nombre = input("Dime tu nombre: ")
print(palabra(tu_nombre))






 
        