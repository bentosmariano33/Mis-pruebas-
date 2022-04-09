def primero_mayor(num1,num2):
    return num1 >= num2

def es_hola_mundo(cadena):
    return  cadena != "Hola mundo"

def son_iguales(cadena1, cadena2):
    cad1_minusculas = cadena1.lower()
    cad2_minusculas = cadena2.lower()

    return cad1_minusculas == cad2_minusculas

def mayor_de_tres(numero1,numero2,numero3):
    if (numero1 > numero2) and (numero1 > numero3):
        return numero1
    elif (numero2 > numero1) and (numero2 > numero3):
        return numero2
    else:
        return numero3

print(mayor_de_tres(10,30,20))



