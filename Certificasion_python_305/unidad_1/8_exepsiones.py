try:
#ejemplo 1 sin manejo de exepsiones
    numero1=float(input("ingresa el primer numero"))
    numero2=float(input("ingresa el segundo numero"))
    resultado=numero1/numero2
    print(resultado)
except zeroDvisionError:
    print("DIVISION ENTRE ZERO ES FALLIDA")
except vuelveerror:
    print("solo introduce numeros")
