# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por
# pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

""" name = input('Cual es tu nombre: ')
num = int(input('Ingresa un numero: '))
print(f'\n{name}' * num)  """


# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por
# pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas
# las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

""" name = input('Cual es tu nombre: ')
print(name.lower())
print(name.upper())
print(name.title()) """


# Ejercicio 3
# scribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
# introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
# mayúsculas y <n> es el número de letras que tienen el nombre.
""" name = input('Cual es tu nombre: ')
print(f'{name.upper()} tiene {len(name)} letras') """


# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el 
# código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa 
# que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin 
# el prefijo y la extensión.
tel = input('Ingrese el numero de telefono con el formato +xx-xxxxxxxxx-xx: ')
print('El numero de telefono sin prefijo ni extension es: ' + tel[4:-3])

