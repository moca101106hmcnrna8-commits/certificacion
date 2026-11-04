promedio=[9,10,6,5,7]
#1. encontear el promedio mas bajo usando el siclo for
#suponemos inicialmente que el promedio mas bajo es el primer elemento
promedio_bajo=promedio[0]
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo = contador
print("el promedio mas bajo es:",promedio_bajo)
#promedio alto
promedio_alto = promedio[0]
for contador in promedio:
    if contador>promedio_alto:
        promedio_alto=contador
print("el promedio mas alto es:",promedio_alto)







