#creando un diccionario en python
persona={
    "nombre":"sofia",
    "edad":28,
    "profesion":"ingeniera",
    "estudiante":False
}
print(persona)
#accediendo a un valor en especifico
print(persona["profesion"])
#se puede usar el metodo . get() .set()
#es util por que no da error si la clave n existe
print(persona.get("edad"))
#modificar un valor exixtente
persona["edad"]=29
print(persona.get("edad"))
#egregar un par (clave:valor)
persona["ciudad"]="san pepe"
print(persona)
#recorrer un diccionario con un bucle 
for clave,valor in persona.items():
    print(f"{clave}:{valor}")