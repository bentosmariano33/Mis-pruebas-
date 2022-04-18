#1. Cree un script que le solicite al usuario ingresar un número por teclado, y
#luego le informe en pantalla si su número es mayor que 10; antes de finalizar
#e independientemente de lo que haya sucedido antes, el script mostrará un
# mensaje de despedida. Ejemplos de cómo debería verse la salida del script:

# 2. Modifique el script anterior para que mantenga el funcionamiento, pero
# ahora, cuando el número no es mayor que 10, también se muestre un
# mensaje “Tu número (N) es menor o igual que 10!”.


from tarfile import REGULAR_TYPES

# num1 = int(input("Ingresa un número: "))
#     if (a > 10):
#         print("Tu número "+str(num1)+" es mayor que 10!")
#     else: 
#         print("Tu número "+str(num1)+" es menor o igual que 10!")

#     print("Saludos!")



# 3. Cree un script que le solicite al usuario ingresar dos números por teclado, y
# luego indique por pantalla cuál de ellos es el mayor. Contemple la posibilidad
# de que los números sean iguales, y muestre un mensaje acorde.

def mayor_que(x,y):
    if (x > y):
        print("Tu número "+str(x)+" es mayor que tu número "+str(y)+" .")
    elif (y > x):
        print("Tu número "+str(y)+" es mayor que tu número "+str(x)+" .")
    else:
        print("Tus números ingresados son iguales.")

numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

mayor_que(numero1,numero2)


# 4. Cree un script que le solicite al usuario ingresar un número por teclado, y le
# informe con un mensaje si su número es positivo, negativo, o 0.

def valor(z):
    if (z > 0):
        print("Su número es positivo.")
    elif (z < 0):
        print("Su número es negativo.")
    else:
        print("Su número es 0.")

valor_user = int(input("Ingresa un número cualquiera: "))
valor(valor_user)

# 5. Cree un script que, dado un número de día de la semana ingresado por
# teclado, muestre el nombre de ese día en lenguaje natural. La relación entre
# números y días de la semana es la siguiente:
# 1 = Domingo.
# 2 = Lunes.
# 3 = Martes.
# 4 = Miércoles.
# 5 = Jueves.
# 6 = Viernes.
# 7 = Sábado.

def dias_de_la_semana(v):
    if (v==1):
        print("Domingo.")
    elif (v==2):
        print("Lunes.")
    elif (v==3):
        print("Martes.")
    elif (v==4):
        print("Miércoles.")
    elif (v==5):
        print("Jueves.")
    elif (v==6):
        print("Viernes.")
    elif (v==7):
        print("Sábado.")

dia = int(input("Ingrese del 1 al 7 un número y le diré que día de la semana es: "))
dias_de_la_semana(dia)

# 6. Cree un script que le solicite a un alumno de la asignatura Introducción a la
# Programación que ingrese las notas de sus dos parciales. Como resultado, se
# le debe informar al alumno su situación, junto con la nota promedio. Las
# reglas para saber la situación de un alumno son las siguientes:
# ● Para estar promovido (es decir, cursada aprobada y no requiere
# rendir final), el alumno debe haber aprobado ambos parciales y
# tener un promedio mayor o igual a 8.
# ● Para estar regular (cursada aprobada, pero debe rendir final), el
# alumno debe haber aprobado ambos parciales (nota mayor o igual
# a 4).
# ● Si el alumno no ha aprobado ambos parciales (es decir, tiene nota
# menor que 4 en alguno de ellos), entonces queda en condición de
# libre (es decir, puede rendir un final extendido o recursar).

def notas(d,e):
    if ((d+e)/2 >= 8):
        print("Su situación es de alumno promovido con un promedio de "+str((d+e)/2)+" .")
    elif ((d+e)/2 >=4):
        print("Su situación es de alumno regular con un promedio de "+str((d+e)/2)+" .")
    else:
        print("Su situación es de alumno libre con un promedio de "+str((d+e)/2)+" .")

nota1 = int(input("Colocá tu primer nota: "))
nota2 = int(input("Colocá tu segunda nota: "))

notas(nota1,nota2)

# 7. Cree un script que determine si un triángulo es isósceles, equilátero, o
# escaleno. Para determinar esto, se le solicitará al usuario ingresar tres
# números, correspondientes a los tres lados del triángulo.
# equilátero = todos los lados iguales
# isósceles = dos lados iguales
# escaleno = todos los lados diferentes

def triangulos(f,g,h):
    if (f==g) and (g==h):
        print("Triángulo equilátero")
    elif ((f==g) and (g!=h)) or ((f==h) and (h!=g)) or ((h==g) and (g!=f)):
        print("Triángulo isósceles")
    elif (f!=g) and (f!=h):
        print("Triángulo escaleno")

lado1 = int(input("Ingrese un lado del triángulo: "))
lado2 = int(input("Ingrese otro lado del triángulo: "))
lado3 = int(input("Ingrese otro lado del triángulo: "))

triangulos(lado1,lado2,lado3)

# 8. Las estructuras alternativas pueden utilizarse para validar datos. Por
# ejemplo, si se intenta crear una función que tome dos enteros como
# parámetro y muestre el resultado de su división, puede ocurrir un error si el
# denominador es cero. Utilice la estructura alternativa para validar que el
# denominador no sea cero; en caso de serlo, la función deberá mostrar el
# mensaje “No se puede dividir por 0!” en lugar de intentar mostrar el
# resultado.

dividendo = int(input("Ingrese su dividendo: "))
divisor = int(input("Ingrese su divisor: "))

def division(numer,denom):
    if (denom != 0):
        print(numer/denom)
    elif (denom == 0):
        print("No se puede dividir por 0!")


division(dividendo,divisor)

# 9. Python ofrece algunas funciones built-in para facilitar la implementación de,
# validaciones. A continuación se listan algunas de las más comunes:
# valor.isdigit()
# Retorna True si todos los caracteres de valor son numéricos, False en caso
# contrario.
# valor.isalpha()
# Retorna True si todos los caracteres de valor son alfabéticos (no
# numéricos), False en caso contrario.
# valor.isalnum()
# Retorna True si valor es una combinación alfanumérica (caracteres y
# números), False en caso contrario.
# Codifique una función que reciba un parámetro cualquiera proveniente del
# usuario del programa (que puede contener letras, números, o una combinación
# de ambas), e indique si el mismo es un número, una palabra, o un valor
# alfanumérico. Compruebe que su función resuelve el problema enviándole
# valores correspondientes a las tres posibilidades.

def palabras(n):
    if n.isdigit():
        print("Es un número")
    elif n.isalpha():
        print("Es una palabra")
    elif n.isalnum():
        print("Es alfanumérico")

cadena = input("Ingrese algo: ")
palabras(cadena)
