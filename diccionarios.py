"""
diccionario = {}
diccionario["nombre"] = "Codi" #agregar una llave con su valor
valor = diccionario["nombre"]
diccionario["nombre"] = 90
print(diccionario)

#si hay dos valores iguales se le asigna el ultimo valor
diccionario = {"a":1, "b":2, "c":3, "a":4}
#obtener elementos de un diccionario
resultado = diccionario["b"]
#otra forma es  y arroja true o false 
resultado = "z" in diccionario
#otra forma es y retorna el valor
resultado = diccionario.get("z", "la llave no existe")
#este metodo arroja los valores que hay en la lsita y si no los agrega
resultado = diccionario.setdefault("z",{})
print(diccionario)
print(resultado)

#Llaves, items, valores
diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
resultado = diccionario.keys()
#tambien podemos visualizarlo como tupla
resultado = tuple(resultado)
resultado = diccionario.values()
resultado = list(resultado)
resultado = diccionario.items()
print(resultado)
"""

#eliminar elementos
diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
del diccionario["a"]
#otra forma es 
valor = diccionario.pop("b")
#eliminar todos los elementos
diccionario = {}
#otra forma es 
diccionario.clear()
print(valor)
print(len(diccionario))
print(diccionario)