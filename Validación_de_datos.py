# nombre = input("Ingrese su nombre: ")

# while not nombre.isalpha():
#     nombre = input("El dato es erróneo.Debe ingresar solo texto.Ingrese su nombre: (Puede presionar # para finalizar el programa)")
#     if nombre == "#":
#         print("Adios")



def datos(nom, edad):
    if nom.isalpha() and edad.isdigit():
        leyenda = "Hola "+ nom + "tu edad es "+ edad
    else:
        leyenda = "El dato es erróneo.Debe ingresar solo texto.Ingrese su nombre: (Puede presionar # para finalizar el programa)"
    return leyenda

def leer_dato():
    return input("Ingrese su nombre: (Puede presionar # para finalizar el programa)")

def validacion():
    centinela = leer_dato()
    while centinela != "#":
        nom = str(centinela)
        print(datos(nom))
        centinela = leer_dato()

validacion()