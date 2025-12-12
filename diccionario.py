personas ={"Nombre":"Rosa","edad":30,"ciudad":"Valencia"}

print(len(personas))
print(personas["edad"])#para acceder a la edad del diccionario
print(personas["Nombre"])#nombre
print(personas["ciudad"])#ciudad


#Para cambiar un valor lo hacemos así
personas["Nombre"]= "Jose"
print(personas["Nombre"])

print(personas.keys()) #Obtengo todas las claves o keys
print(personas.values())#Obtengo los valores
print(personas.items())#Obtengo valor y clave
print(personas.get("ciudad"))#Hace una búsqueda de un valor por su key, si damos una key que no existe nos tira un None
print(personas.pop("edad"))#Nos elimina un elemento por su key
print(personas)
print(personas.update({"pais":"España"}))#Añade un elemento nuevo
print(personas)

for k,v in personas.items():
    print(f"key : {k}, value: {v}")