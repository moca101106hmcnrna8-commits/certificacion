try:
    alumno=["martin", "fani", "samuel","angel eduardo","alma","lucerona","venegas","dulce","daniel","yexalen"]
    calificaciones = [10, 9, 8, 7, 8, 9, 10, 9, 6, 7]
    print(alumno[2], calificaciones[2])
    print(alumno[4], calificaciones[4])
    print(alumno[6], calificaciones[6])
    print(alumno[8], calificaciones[8])
    print(alumno[10], calificaciones[10])
except IndexError:
    print("indice incorecto")