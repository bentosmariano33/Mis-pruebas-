base = 8
altura = 2

def area_rectangulo(b, a):
    resultado = 0
    resultado = b*a
    return resultado

Z = area_rectangulo(base, altura)

print(Z)  #imprimir con variable creada.
print(area_rectangulo(base, altura)) #imprimir sin variable, llamando solo la función.





#Escriba una función que reciba dos enteros como parámetro, y luego retorne el resultado de la suma.
#Intput = ent1, ent2 (int)
#Output = suma (int)

def resultado_suma(ent1, ent2):
    suma = ent1 + ent2
    return suma
  

#test
def test_resultado_suma():
    print("Testeando la suma...")
    assert resultado_suma(2,2) == 4
    assert resultado_suma(1,1) == 2
    print("Testeado OK!")

test_resultado_suma()


#CONTINUACIÓN
#Modifique la función para que en lugar de retornar el resultado, lo muestre en pantalla.

#CONTINUACIÓN (2)
#Pruebe invocar a la función utilizando dos valores leídos desde teclado
