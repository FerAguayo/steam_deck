"""
def saludar():
    #Bloque de código que pertenece a la función saludar
    print("Hola")


#La invocación de función en python siempre con paréntesis

saludar()

def ver_numero():

    return 150

a=10;b=5;c=a+b

suma = c + ver_numero()

print("La suma es: ", suma)

saludo = "Hola, como vas"
#funcion con parámetros de entrada
def saludocustom(saludo):
    print(saludo)#Los parámetros de entrada que declaremos sólo pertenecen a la función
    #Es decir, solo se puede usar dentro de la función

saludocustom("Hey! How you doing! ")

def datosCliente(nombre,apellido,email,telefono):
    datos_cliente = f"Nombre: {nombre}\nApellido: {apellido}\nEmail: {email}\nTeléfono: {telefono}"
    # las "f strings" es una manera de concatenar cualquier variable a la cadena
    # \n nos permite hacer saltos de linea 
    print(datos_cliente)

datosCliente("Pepe","Perez","asd@qwe.com","654654654")

def calcularCuadrado(num:int|float)-> int|float:


    return num*num
#try y except es una manera de comprobar fallos
try:
     print(calcularCuadrado("asdasd"))
except Exception as e:
    print("Uuy! Lo siento debes ingresar un número!!")

"""

