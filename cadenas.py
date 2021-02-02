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
""" tel = input('Ingrese el numero de telefono con el formato +xx-xxxxxxxxx-xx: ')
print('El numero de telefono sin prefijo ni extension es: ' + tel[4:-3]) """

# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla 
# la frase invertida.
""" frase = input('Ingrese una frase: ')
print('Frase invertida: ' + frase[::-1]) """

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después 
# muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
""" frase = input('Ingrese una frase: ')
vocal = input('Ingrese una vocal: ')
print(frase.replace(vocal.lower(), vocal.upper())) """

# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
# pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con 
# dominio ceu.es.
""" email = input('Ingrese un correo electronico: ')
new_email = email[:email.find('@')+1]  + 'ceu.es'
print('Nuevo correo: ' + new_email) """

# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
# y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
""" precio = input('Ingresa el precio en euros con dos decimales: ')
entero = precio[:precio.find('.')]
decimales = precio[precio.find('.')+1:]
print(f'El precio es {entero} euros con {decimales} centimos') """

# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
# y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
# funcione cuando el día o el mes se introduzcan con un solo carácter.
""" fecha_nac = input('Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ')
fecha = fecha_nac.split('/')
print(f'Dia: {fecha[0]} Mes: {fecha[1]} Año: {fecha[2]} ') """

# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
productos = input('Ingrese los productos separados por comas: ')
for producto in productos.split(','):
    print(producto.strip())
# solucion 2
# print(productos.replace(',', '\n'))    

# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades 
# y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario 
# con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total 
# con 8 dígitos enteros y 2 decimales.