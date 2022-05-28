# def webinars(n):
#     mayor_inscriptos = 0
#     total_de_inscriptos = 0
#     titulo_mayor_inscriptos = "No hubo inscriptos"
#     for i in range(n):
#         título = input("Ingrese el título del Webinar: ")
#         inscriptos = int(input("Ingrese la cantidad de inscriptos: "))
#         total_de_inscriptos += inscriptos

#         if inscriptos > mayor_inscriptos:
#             mayor_inscriptos = inscriptos
#             titulo_mayor_inscriptos = título

#     if n>0:
#         promedio = total_de_inscriptos / n
#         print(promedio)
#         print(titulo_mayor_inscriptos)


# webinars(2)

datos_validos = False

while not datos_validos:
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")

    if nombre.isalpha() and edad.isdigit() and int(edad) > 18 and int(edad) < 99:
        datos_validos = True
        print(f"Hola {nombre}, tu edad es {edad}")
    elif datos_validos == False:
        print("Datos erroneos")
        datos_erroneos = input("* para cerrar el programa")
        if datos_erroneos == "*":
            print("Adios")



