edad=int(input("introduce tu edad"))
if edad >= 0 and edad <= 3:
    print("ERES BEBE")
elif edad >= 4 and edad <= 11:
    print("ERES UN NIÑO")
elif edad >= 12 and edad <= 18:
    print("eres un adolecente")
elif edad >= 19 and edad <= 29:
    print("ERES UN JOVEN")
elif edad >= 30 and edad <= 40:
    print("ERES UN ADULTO")
elif edad >= 41 and edad <= 100:
    print("ERES UN CHAVO RUCO!")
else:
    print("estas rrobando oxijeno")
