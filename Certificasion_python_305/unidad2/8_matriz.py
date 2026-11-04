#creando una matriz
matriz=[
    [5,8,1],#fila 1 x 3 columnas
    [3,9,2]#fila 2 x 3 columnas 
]
#obteniendo el numero total de filas y columnas
#filas=len(matriz)
#columnas=len(matriz[0])
#ciclo externo para los indices de las filas(1)
for i in range(0,2):
    #ciclo interno para los indicecs de las columnas(j)
    for j in range(0,3):
        print(f"pocicion[{i}][{j}]={matriz[i][j]}")
