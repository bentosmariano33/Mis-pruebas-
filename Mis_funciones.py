str = "PyTHON"

print(str[-6:6])
print(str[::-1])


print(type("Hola mundo"))
print(type("100"))
print(type(100))


# 8. Escribir una función que reciba una cadena que contiene un largo número
# entero y devuelva una cadena con el número y las separaciones de miles. Por
# ejemplo, si recibe '1234567890', debe devolver '1.234.567.890'.

# def transformer(x):
#     x.replace("x", 3)
#     return x

# transformer('1234567890')

# replace()



# def separar_miles(cad):
#     cad2=""
#     cont=1
#     for caracter in cad[::-1]:
# 	    cad2=caracter+cad2
#         if cont%3==0:
#             cad2="."+cad2
#             cont=cont+1
#     return(cad2)


# 1. Diseñe una función que reciba una lista, vacía o no, e incorpore números hasta que
# el usuario ingrese el valor “salir”. Cuando termina de ingresar los datos, la
# función debe retornar la lista al programa principal.


#INPUT: s(list)
#OUTPUT:  t (lsit)
#La función incorpora numeros a s hasta que el usuario ingresa el valor "Salir" y retora la lista.
def numeros_listados (s):
    elemento = input("Ingrese un elemento (salir para terminar): ")
    while elemento != "salir":
        s.append(elemento)
        elemento = input("Ingrese un elemento (salir para terminar): ")
    return s

a = []
numeros_listados(a)
for elem in a:
    print(elem)

# 2. Dada una lista de números enteros, escribir una función para cada uno de los
# siguientes ítems:
# a- Devuelva una lista con todos los números que sean primos.
# b- Devuelva la sumatoria y el promedio de los valores.
# c- Devuelva una lista con el factorial de cada uno de esos números.


# INPUT: s (list[int])
# OUTPUT: sumatoria(int), promedio(float)

def suma_y_promedio(s):
    suma = 0
    prom = 0
    cantidad_elem = len(s)
    for i in s:
        suma += i
    if cantidad_elem != 0:
        prom = suma/cantidad_elem
    return suma, prom


def test_suma_y_promedio():
    print("Testeando suma_y_promedio...")
    assert suma_y_promedio([])== (0,0)
    assert suma_y_promedio([2,4]) == (6,3.0)
    assert suma_y_promedio([-2,4]) == (2,1.0)
    print("Pasó")

test_suma_y_promedio()

#INPUT: s(list[int])
#OUTPUT: t(list[int])
#La lista t es una lista con el factorial de cada uno de los números de s

def factorial(s):
    t = []
    for i in s:
        t.append(factorial(i))
    return t

# def test_factorial():
#     print("Testeando factorial...")
#     assert factorial([])== (0,0)
#     assert factorial([2,4]) == (6,3.0)
#     assert factorial([-2,4]) == (2,1.0)
#     print("Pasó")

test_factorial()