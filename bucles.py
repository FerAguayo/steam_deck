"""Hay 2 tipos de bucles en programación
        for y while
for es una estructura que 


while nos permite realizar múltiples iteraciones basándonos 
en el resultado de una expresión lógica
        """

#While repite el bloque de código mientras la condición sea verdadera
"""
while True:
    print("hola")
"""
#Esta función nos daría un número infinito(Hasta que se queda sin recursos) de "hola"
"""
seguir = True

while seguir:
    print("Esto funciona!")

    fin = input("Desea seguir con este while? Y/n ")
    if fin == "n":
        seguir = False
        print("Esto se ha acabado")
"""

#While con else
"""
nombre = "María"
while nombre == "María":
    print("Hola ", nombre)
else:
    print("Tú no eres María!")
"""

#Imprimir valores del 1 al 100
"""
count = 0
while count <= 100:
    count += 1
    print(count)
"""

#Bucle for, se repite mientras se cumpla el número de iteraciones definidas
#metodo deltro del for range( inicio, final(el número dado -1), salto(opcional))
#imprimir valores del 1 al 10
"""
for iteracion in range(1,101):
    print(iteracion)
"""
#realizar un programa que muestre la tabla de multiplicar dado un número
"""
def TablaDeMultiplicar(numero):

    # numero = int(input("Introduce un número: "))
    numero = int(numero) # <- es lo mismo que ponerlo entre paréntesis como arriba
    # pero para mayor entendimiendo es hacerlo ordenado 
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

TablaDeMultiplicar(10)

"""

#Ahora con while

def TablaDeMultiplicar(numero):

    # numero = int(input("Introduce un número: "))
    numero = int(numero) # <- es lo mismo que ponerlo entre paréntesis como arriba
    # pero para mayor entendimiendo es hacerlo ordenado 
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

    
seguirMultiplicando = True

while seguirMultiplicando:
    num = input("Introduce un númer: ")
    TablaDeMultiplicar(num)

    valor = input("Desea seguir multiplicando) s/n")


    #TERMINAR MIRANDO EL VIDEO