# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
""" print('¡Hola Mundo!') """

# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla 
# el contenido de la variable.
""" msg = '¡Hola Mundo!'
print(msg) """

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el 
# usuario haya introducido.
""" name = input('Cual es tu nombre: ')
print(f'¡Hola {name}!') """

# Ejercicio 4
# Escribir un programa que realice la siguiente operación aritmética .
""" print(((3+2)/(2*5))**2) """

# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.
""" horas_trabajadas = int(input ('Ingrese el numero de horas trabajadas: '))
costo_por_hora = float(input('Ingrese el costo por hora: '))
print('El pago es: ' + str(horas_trabajadas*costo_por_hora))
 """
# Ejercicio 6
# Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en 
# pantalla la suma de todos los enteros desde 1 hasta n. 
""" n = int(input('Ingrese un entero positivo: '))
suma_1_n = int(n*(n+1)/2)
print(f'La suma de todos los enteros desde 1 hasta {n} es: {suma_1_n}') """


# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice 
# de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa 
# corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

""" peso = float(input ('Ingresa tu peso en kg: '))
estatura = float(input ('Ingresa tu estatura en metros: '))
imc = peso / estatura
print(f'Tu IMC es {imc:.2f}') """

# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> 
# da un cociente <c> y un residuo <r> donde <n> y <m> son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.
""" primer_numero = int(input('Ingrese el primer numero: '))
segundo_numero = int(input('Ingrese el segundo numero: '))
cociente = primer_numero // segundo_numero
residuo = primer_numero % segundo_numero

print(f'{primer_numero} entre {segundo_numero} da un cociente de {cociente} y un residuo de {residuo}') """

# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número
# de años, y muestre por pantalla el capital obtenido en la inversión.
""" inversion = float(input('Ingrese la cantidad a invertir: '))
interes_anual = float(input('Ingrese el interés anual, ej. 10: '))/100
anios = int(input('Ingrese la cantidad de años: '))
monto_final = inversion * ((1+interes_anual)**anios)
print(f'El capital obtenido al finalizar el periodo será: {monto_final:.2f}') """
# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por 
# correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso 
# de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada 
# muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último 
# pedido y calcule el peso total del paquete que será enviado.
""" peso_payaso = 112
peso_muneca = 75
cant_payasos = int(input('Ingrese el numero de payasos vendidos: '))
cant_munecas = int(input('Ingrese el numero de muñecas vendidas: '))
peso_total = round((peso_payaso*cant_payasos)+(peso_muneca*cant_munecas),2)
print(f'El peso total del pedido es: {peso_total}gr') """

# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
# final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
# depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear 
# cada cantidad a dos decimales.
interes_anual = 0.04
monto_inicial = float(input('Ingrese el monto inicial de la cuenta de ahorros: '))
for anio in range(1,4):
    monto_anual = round(monto_inicial * ((1+interes_anual)**anio),2)
    print(f'El monto al final del año {anio} es {monto_anual:.2f}')

# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento 
# del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del 
# día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que 
# se le hace por no ser fresca y el coste final total.

""" precio_unitario = 3.49
descuento = 0.6
barras_vendidas = int(input('Cuantas barras no frescas se vendieron: '))
monto_ahorrado = round(barras_vendidas * precio_unitario * descuento,2)
costo_final = round(barras_vendidas * precio_unitario * (1-descuento),2)
print(f'El precio habitual de una barra de pan es: {precio_unitario}€')
print(f'El descuento por no ser una barra de pan fresca es de {descuento*100}%')
print(f'El monto ahorrado es {monto_ahorrado}€')
print(f'Costo final: {costo_final}€') """