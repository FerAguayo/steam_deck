#A las listas se les puede llamar lista, array o contenedor

#la longitud de una lista se cuenta con len(lista) y nos devuelve un entero

lista_all = ["Maria", 10, True, 3.99,[1,2,3]]
"""
print(len(lista_all)) #obtener la longitud de la lista
print(lista_all[0])#obtener el valor de la primera posición
print(lista_all[-1])#obtener el valor de la ultima posición
print(lista_all[len(lista_all)-1])#obtener el valor de la ultima posición
"""

#Podemos cambiar los datos 
"""
lista_all[0] = "Juana"
print(lista_all)
"""

"""
print("#Lista con for")
for valores in lista_all:
    if valores == True:
        print("Bool encontrado: ", valores)
"""
"""
#Para buscar en iteraciones usar este método
for iteracion in range(0,len(lista_all)):
    if iteracion == 3:
        print(lista_all[iteracion])

print("Recorrer lista con while")
count = 0
while count < len(lista_all):
    print(lista_all[count])
    count += 1
"""

print("recorrer un string")

for i in "Paula Valiente":
    if i == "V":
        print("Existe V", i)

