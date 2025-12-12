"""
Operaciones aritméticas
Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

Restricciones
Convertir las cadenas de entrada en números
Separar convenientemente la entrada, transformación de cadena en números y salida separados
Crea una única sentencia de salida con los saltos de línea adecuados (sólo un print)

Retos

1.Controla que las entradas sean números de forma que el programa no avance si no se introduce un número

2.No permitas introducir números negativos
"""


#Entrada
numero1 = (input("Ingrese el primer número: "))
numero2 = (input("Ingrese el segundo número: "))

#Control

while not(numero1.isnumeric()) and not(numero2.isnumeric()) :

    print("Esta función solo admite números positivos, por favor ingrese los datos de nuevo: ")
    numero1 = (input("Ingrese el primer número: "))
    numero2 = (input("Ingrese el segundo número: "))



#Transformación
numero1 = float(numero1)
numero2 = float (numero2)


#Salida
print(f"La suma es: {numero1 + numero2}\nLa resta es: {numero1 + numero2}\nLa multiplicación es: {numero1 * numero2}\nLa división es: {numero1 / numero2}")


