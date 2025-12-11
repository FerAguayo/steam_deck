# <- comentarios de una línea
"""
Comentario en
varias líneas
"""
'''
Comentario en
varias líneas
'''


#Salida de información
print("Hola python")

#Entrada de información
nombre = input("Ingrese su nombre ")
#Un input siempre devuelve un string


#Variables (siempre tienen que tener un valor)
#Son case sensitive -> Hola != hola
variable = "Su nombre es "

print (variable+nombre)

print(type(variable))

#Tipos de variables 
#str "Hola :D" 'Pueden ir con comillas simples y dobles' 
#int 1,2,3,4,5
#float 1.2,1.3,1.4
#bool True or False

"""Reglas de nombre de variables"""
#Los nombre de Variables y funciones van en minúscula
#Los nombres de clases con la primera en mayúscula
#Los nombre de Variables constantes en mayúscula
"""No se puede"""
#Poner variables con números antes de letra
#Espacios

"""Sí se puede"""

nombre02 = "María"
#Se recomienda usar el estilo de declaracion snake case o camel case
#snake case -> nombre_02
#camel case -> nombre-02

#Casting o casteo: convertir un tipo de variable en otro

numero1 = "100"
numero2 = 50

suma = numero2 + int(numero1)

print ("La suma es: " + str(suma))