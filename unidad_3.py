# Escriba una función que reciba dos enteros como parámetro, y luego retorne el resultado de la suma.
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero entero: "))

#Defino la nueva función
def suma(a,b):
    resultado = a + b
    print(resultado)

    
x = suma(a,b) #Vinculo la función a una variable

print(x) #Llamo a la variable creada.

# CONTINUACIÓN
# Modifique la función para que en lugar de retornar el resultado, lo muestre en pantalla.

# CONTINUACIÓN (2)
# Pruebe invocar a la función utilizando dos valores leídos desde teclado.



#test
# def test_suma():
#      print("Testeando la suma...")
#      assert suma(2,2) == 4
#      assert suma(1,1) == 2
#      print("Testeado OK!")

# test_resultado_suma()