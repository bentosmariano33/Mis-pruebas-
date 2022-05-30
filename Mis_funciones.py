from dataclasses import replace


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



def separar_miles(cad):
    cad2=""
    cont=1
    for caracter in cad[::-1]:
	    cad2=caracter+cad2
        if cont%3==0:
            cad2="."+cad2
            cont=cont+1
    return(cad2)