colores=["azul","morado","rojo","amarillo","verde"]
print=input("ingresa el color:")#naranja
encontrado=False
for contador in colores:
    print(contador)
    print(contador)
#si el color actual es "rojo detener el bucle"
    if contador==color:
        print("color encontrado! saliendo de el bucle")
        encontrado=True
        break
if not  encontrado:
    print("el color,",color," nose encontro")