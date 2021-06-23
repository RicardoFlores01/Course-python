"""
variable = None #lo toma como valor falso 
print(variable)
"""

#condicion
"""
color_luz = 'amarillo'
if color_luz=='verde':
	print('puede continuar')
elif color_luz == 'amarillo':
	print('Alto parcial')
else:
	print('Alto total')
"""

"""
#Condiciones con booleanos
variable = False
if variable:
	print('Es verdadero')
else:
	print('Es falso')

#valores de falso 
# False, "", '', [], {}, 0, 0.0
"""

#Ciclos con while 
"""
numero = 123456789
contador = 0

while numero >= 1:
	contador+=1
	numero = numero / 10
else:
	print("La cantidad de digitos del numero es ",contador)
"""

"""
#Ciclo for
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
	print(numero)

"""

"""
#iterar diccionario 
diccionario = {'a':1, 'b':2}
for llave in diccionario:
	print(llave)
"""

"""
#recorrer tuplas que almacena tuplas y listas dentro
valores = ( (10,20), ["strings","strings"], (True, False) )
for valor in valores:
	print(valor)

#quitando parentesis o corchetes
valores = ( (10,20), ["strings","strings"], (True, False) )
for valor1, valor2 in valores:
	print(valor1, valor2)


#recorrer rangos puede ser de uno inicial y otro final
for valor in range(1,20):
	print(valor)


#for en listas
lista = [1,2,3,4,5,6]
for indice in range( len(lista) ):
	print("Indice:",indice, "valor:", lista[indice])

"""

"""
#break y continue
titulo = "Curso de Python 3"
for caracter in titulo:
	if caracter == "P":

		# continue no aparece la letra P
		# break se corta, de aqui en adelante no aparece lo demas
	print(caracter)
"""

#asignacion de valores mediante if
calificacion = int(input("Dame tu calificacion: "))
color = None
if calificacion >= 7:
	color = 'verde'
else:
	color = 'rojo'
print(calificacion, color)
