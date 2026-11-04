#1. creamos un diccionario
nuevo_usuario={}
#2. pedimos los datos desde el teclado 
nuevo_usuario["nombre"]= input("ingresa el nombre:")
nuevo_usuario["edad"]= int(input("ingresa la edad:"))
nuevo_usuario["estatura"]= float(input("ingresa tu estatura en metros:"))
print("\n ---imformasion guardada---")
#mostrando la imformasion de el diccionaro
print(nuevo_usuario)