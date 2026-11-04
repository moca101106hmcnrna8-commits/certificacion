#matrix
matriz=[
    ["A","B","C",],
    ["D","E","F",],
    ["G","H","I",],
    ["J","K","L",],
    ["M","N","Ñ",],
    ["O","P","Q",],
    ["R","S","T",],
    ["U","V","W",],
    ["Y","Z","T",],
]
for i in range(0,9):
    #ciclo interno para los indicecs de las columnas(j)
    for j in range(0,3):
        print(f"pocicion[{i}][{j}]={matriz[i][j]}")
