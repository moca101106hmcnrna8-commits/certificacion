#ciclo externopara el numerode la base de la tabla
for i in range(1,4):
    print(f"---tabla de el {i}")
    #ciclo interno para multiplicar de el 1 al 10
    for j in range(1,11):
#1(i) x 1(j)=1
        print(f"{i} x {j} = {i*j}")
    print(F"AQUI TERMINA LA TABLA DEL {i}")
    #aqui termina el ciclo externo