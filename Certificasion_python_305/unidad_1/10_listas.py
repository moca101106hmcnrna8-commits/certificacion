try:
    #declarando una lista
    materias=["programacion", "Filosofia", "matematicas","Igles"]
    print(materias[0])
    materias.append("lengua y comunicasion")
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("matematicas")
    print(materias)
except indexerror:
    print("indice incorrecto")