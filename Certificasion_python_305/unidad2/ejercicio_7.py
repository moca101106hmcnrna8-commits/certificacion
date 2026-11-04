#el mapa de el tesoro
mapa=[
    [".",".",".","."],
    [".",".","X","."],
    [".",".",".","."],
    [".",".","B","."]
]
filas=len(mapa)
columnas=len(mapa)
#recorriendo la matriz con ciclos animados 
#ciclo externo para amnejar filas(i)
for i in range(filas):
    #ciclo externo para manejar columnas (j)
    for j in range (columnas):
        #verificamos si encontramos el tesoro
        if mapa [i][j]=="X":
            print(f"tesoro encontrado en la pocicsion[{i}][{j}]")
        if mapa [i][j]=="B":
            print(f"tesoro encontrado en la pocicsion[{i}][{j}]")