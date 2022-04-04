def leer_cadena():
    string = input("Ingrese su texto: ")
    return string

def test_leer_cadena():
    print("Testeando la función leer_cadena()...")
    assert leer_cadena() == "Marcos"
    assert leer_cadena() == "Matias"
    assert leer_cadena() == "Mariano"
    print("Pasó!")

test_leer_cadena()

    