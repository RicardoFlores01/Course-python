"""
cursos = ["python","django","flask","c","c++","c#","java","php"]
#curso = cursos[2]
#del cero hasta el indice 3
sub = cursos[0:3]
#del suindice 3 hasta el ultimo 
sub = cursos[5:]
#todos los elementos de la lista
sub = cursos[:]
#con saltos, del subindice 1 hasta el 6 pero de dos en dos 
sub = cursos[1:7:2]
#el inverso de la lista
sub = cursos[::-1]
print(sub)
"""
#OPERACIONES COMUNES 
"""
lista = [8.17,90,1,5,44,1.32]
lista.sort() #forma ascendente
lista.sort(reverse=True) #forma descendente
mayor = lista[0] #Obtener el numero mas grande
menor = min(lista) #Obtener numero menor
mayor1 = max(lista) #obtener mayor
longitud = len(lista) #Obtener la longitud
resultado = 8.17 in lista #buscando elementos
indice = lista.index(8.17) #arroja donde se encuentra el indice
contador = lista.count(5) #arroja cuantas veces se encuentra el numero en la lista
print(resultado)
"""

#MATRICES 
"""
fila_uno = [10,20]
fila_dos = [30,40]

matriz = [fila_uno, fila_dos]

primer_elemento = matriz[0][0]
print(primer_elemento)
"""

"""
#Otros metodos
.clear() elimina todos los elementos de la lista 
.append agrega un elemento al final de la lista
.insert te permite agregar un elemento en la lista en la posición que tu desees
.remove te permite eliminar el primer elemento que coincida con el que tu quieras eliminar
"""

#TUPLAS
"""
tupla = (1,2,3,4,5,6,7,8,9,0)
#del cero hasta el indice 3
sub = tupla[0:3]
#del suindice 3 hasta el ultimo 
sub = tupla[5:]
#todos los elementos de la lista
sub = tupla[:]
#con saltos, del subindice 1 hasta el 6 pero de dos en dos 
sub = tupla[1:7:2]
#el inverso de la lista
sub = tupla[::-1]

#NOTA, una vez declarada la tupla no se puede modificar
tupla = (1,2,3,4)
uno, dos, tres, cuatro = tupla

#Generar tuplas de las listas
tupla = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]
tupla_dos = (100,200,300,400)

resultado = zip(tupla,lista, tupla_dos)
resultado = tuple(resultado)
print(resultado)
"""

#De listas a tupla 
lista = ["Curso","Python","CodigoFacilito"]
tupla = ("Introduccion","Basico","Listas","Tuplas")

#tupla a listas 
nueva_lista = list(tupla)
print(nueva_lista)

#lista a tupla 
nueva_tupla = tuple(lista)
print(nueva_tupla)

mensaje = "Este es el nuevo curso de python"
mensaje_lista = list(mensaje)
mensaje_tupla = tuple(mensaje)
