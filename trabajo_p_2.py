# Utilizando el editor de código que prefiera, cree un script llamado hola_mundo.py que realice las mismas operaciones que en el ejercicio anterior. 
# Guarde el script y ejecútelo (mediante una terminal, o la IDE que esté utilizando). 

print("HOLA MUNDO")
print(3 + 4)

# 3. Cree un nuevo script llamado pruebas.py, y luego copie y pegue el siguiente contenido: 
# pint('Esto es una prueba') 
# print(10 - 1) 
# Ejecute el script. ¿Qué ha sucedido? Lea detenidamente el error, e intente descubrir qué nos está diciendo el intérprete de Python. 
# ¿En qué línea está el error? ¿Puede corregirlo?

print('Esto es una prueba') 
print(10 - 1)

# 4. Un colega programador nos ha proporcionado un script que resuelve la multiplicación de dos números y muestra el resultado en pantalla; 
# el contenido del script es el siguiente: 

numero1 = 10 
numero2 = 5 
resultado = numero1 * numero2 
print('El producto entre ' + str(numero1) + ' y ' + str(numero2) + ' da ' + str(resultado)) 

# Ejecute el código para verificar el funcionamiento del script, y luego analice detenidamente el código y responda: 
# - ¿Qué son numero1, numero2, y resultado? 
# - ¿Por qué es necesario utilizar la función str(...) para mostrar en pantalla los valores de numero1, numero2, y resultado? 

# 5. Cree un script llamado mi_nombre.py, el cual almacene su nombre completo
# en una variable, y luego lo muestre en pantalla. 

nombre = "Mariano Ezequiel Bentos"
print(nombre)

# 6. Modifique el código del ejercicio anterior para que el nombre se almacene en una variable, y el apellido en otra. Además, introduzca una tercera variable para almacenar su edad. 
# Ahora, en pantalla muestre el mensaje “Mi nombre completo es [NOMBRE] [APELLIDO] y tengo [EDAD] años.”. 

nombre = "Mariano Ezequiel"
apellido = "Bentos"
edad = 29
print("Mi nombre completo es ", nombre, apellido, " y tengo ", str(edad), " años.")

# 7. Cree un script llamado numero_favorito.py, y almacene su número favorito en una variable. Luego muestre en pantalla el mensaje “Mi número favorito es [N]”.

#Almaceno mi núm favorito en la variable num_favorito
num_favorito = 15

#Muestro en pantalla la frase solicitada. 
print("Mi número favorito es ", num_favorito)