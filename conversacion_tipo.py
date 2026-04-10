nombre_personal1 = input("Ingrese su nombre: ")
saludo = "Buen día "
print(type(nombre_personal1))
print(nombre_personal1)
# CONCATENACIÓN de cadenas de texto
print(saludo + nombre_personal1)

str_numero_entero = input("Ingrese un número entero: ")
numero_entero = int(str_numero_entero)
numero_decimal = float(str_numero_entero)
print(type(numero_entero))
print(type(numero_decimal))
print(numero_entero)
print(numero_decimal)

numero_uno = 25
numero_dos = 50

#  La operacion + con 2 numeros, opera aritmeticamente sumandolos y entregando el resultado
print(numero_uno + numero_dos)
#  La operacion + con 2 numeros, opera semanticamente concatenandolos y entregando el string resultante
print(str_numero_entero + numero_dos)

print(numero_dos + str_numero_entero)
