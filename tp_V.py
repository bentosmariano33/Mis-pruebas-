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
    """
    INPUT: p (string)
    OUTPUT: cont_letras (int)
    La variable cont_letras es la cantidad de letras.
    """
    cont_letras = len(p) #cuenta las letras de la palabra colocada como p
    return cont_letras

nombre_usuario = input("Ingrese su nombre: ")
print(palabra(nombre_usuario))

#Test de la función creada
def testpalabra():
    print("Testeando función palabra()...")
    assert palabra("Hola") == 4
    assert palabra("") == 0
    assert palabra("Hola mundo!") == 11
    print("Pasó!")

testpalabra()

# 4. Cree una función que reciba dos números como parámetro (base y exponente), 
# y retorne el resultado de elevar base a la potencia exponente. 

def potencia(base, exponente):
    resultado = base**exponente
    return resultado

base = int(4)
exponente = int(3)
print(potencia(base,exponente))
    
# 5. Cree una función que reciba un string como parámetro, y retorne el mismo string, 
# pero con todas las letras convertidas a mayúsculas.
# 6. Modifique la función del ejercicio anterior para que retorne dos versiones del 
# string recibido como parámetro: primero la versión en minúsculas, y luego la versión en mayúsculas.

def texto(nombre):
    nombre_min = nombre.lower() #muestra el nombre en minuscula.
    nombre_max = nombre.upper() #muestra el nombre en mayuscula.
    return nombre_min, nombre_max

print(texto("Emiliano"))


# 7. Cree una función que reciba dos string como parámetro (nombre1 y nombre2), 
# y retorne True si nombre1 tiene más letras que nombre2, o False en caso contrario.


def nombres(nombre1, nombre2):
    """Nos muestra la verdad de que nombre1 es mas largo que nombre2"""
    comparar_letras = len(nombre1) > len(nombre2) #Compara si el nombre1 es mayor en letras que el nombre2.
    return comparar_letras

print(nombres("Martin", "Jose"))

# 8. Cree un archivo llamado modulo_cadena.py; dentro de él, 
# cree una función llamada leer_cadena que, sin recibir ningún parámetro, 
# le solicite al usuario leer un string cualquiera, y luego lo retorne. 
# Luego cree otro archivo llamado programa_principal.py, que ejecute el programa haciendo uso de la función
# creada en el otro archivo.






 
        