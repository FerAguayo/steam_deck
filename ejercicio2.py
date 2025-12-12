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

seguir = True
while seguir:
    #Entrada
    numero1 = (input("Ingrese el primer número: "))
    numero2 = (input("Ingrese el segundo número: "))
    operacion = (input("Qué deseas hacer? +,-,* o /"))

    #Control
    while operacion not in "+-*/":
        print("Caracter de operación no válido, vuelva a ingresarlo")
        operacion = (input("Qué deseas hacer? +,-,* o /"))

    while not(numero1.isnumeric()) and not(numero2.isnumeric()) :

        print("Esta función solo admite números positivos, por favor ingrese los datos de nuevo: ")
        numero1 = (input("Ingrese el primer número: "))
        numero2 = (input("Ingrese el segundo número: "))



    #Transformación
    numero1 = int(numero1) or float(numero1)
    numero2 = int(numero2) or float (numero2)


    #Salida
    resultado = 0
    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        resultado = numero1 / numero2
    print(f"{numero1}{operacion}{numero2}={resultado}")

    continuar = input("Desea seguir utilizando la calculadora? Y/n: ")
    if continuar == "n":
        seguir = False
        print("Fin de la aplicación")


