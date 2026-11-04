#cadenas y contatesion con(+)
cadena1='hola'
cadena2=" mundo"
multilineas=""" esto es una cadena 
de varias lineas"""
print(cadena1 + cadena2  + multilineas)
#cadena y repeticion 
eco="ja"*3
print(eco)
#cambiar una acdena de minusculas a myusculas
tu_nombre='Angel Eduardo'
print(tu_nombre.upper())
#cambiar de mayusculas a minusculas
print(tu_nombre.lower())
#remplazar un texto en una cadena
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de concatenar cadenas (F-string)
edad=15
nombre='Angel'
mensaje=f"hola,me llamo {nombre} y tengo\n{edad}años"
print(mensaje)
#contar las caractersticas de una cadena 
texto= "!felicidades por continuar en CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra 
oracion="aprender python es divertido"
if "python" in oracion:
    print("encontardo")
else:
 print("no esta")
#validar contenidoo de una cadena 
ncadena="a1"
print(ncadena.isalpha())#true
print(ncadena.isdigit())#false