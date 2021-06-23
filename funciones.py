"""
#creando primer funcion
def saluda():
	print("Hola Mundo!")

saluda()
"""
"""
def crear_mensaje(nombre):
	mensaje = "Hola {}, Bienvenido al curso de Python 3".format(nombre)
	return mensaje

def suma(v1, v2, v3):
	return v1 + v2 + v3

def obtener_curso():
	return "Curso de Python", "Basico", 3.6

nuevo_mensaje = crear_mensaje("Rick")
print(nuevo_mensaje)

resultado = suma(10,20,30)
print(resultado)

curso, nivel, version = obtener_curso()
print(curso, nivel, version)
"""

#RECIBIR N CANTIDAD DE PARAMETROS 
"""
def crear_usuario(nombre, apellido, edad=10):
	return {
		'nombre' : nombre,
		'apellido' : apellido,
		'nombre_completo' : "{} {}".format(nombre, apellido),
		'edad' : edad
	}

codi = crear_usuario("Codigo", "Facilito")
print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])
"""

#Args keyword
#significa que cuando no sabes cuantos parametros 
#tendra se pone *args
"""
def suma(*args):
	total = 0
	for valor in args:
		total +=valor
	return total

resultado = suma(10,20,30)
print(resultado)

def usuarios_autenticados(**kwargs):
	print(kwargs)

usuarios_autenticados(codi=True, facilito=False)
"""

#Alcance global 
"""
animal = 'Leon'

def mostrar_animal():
	global animal
	animal = 'Ballena'
	print(animal)

mostrar_animal()
print(animal)
"""

#Expresiones lambdas 
"""
def centigrados_a_farhenheit(grados):
	return grados * 1.8 + 32

funcion_variable = centigrados_a_farhenheit
resultado = funcion_variable(32)
print(resultado)

#es la misma pero mas simplificada

mi_funcion = lambda grados=0 : grados * 1.8 + 32
resultado = mi_funcion(32)
print(resultado)
"""

# Funciones anidadas
"""
def comenzar_play_list(lista):
	def reproducir():
		for val in lista:
			print(val)
	reproducir()
lista = ['track 1','track 2','track 3','track 4']
comenzar_play_list(lista)
"""

#Decoradores, cambiar una funcion existente
#a(b) -> c (a, b y c son funciones)

def decorador(funcion):
	def nueva_funcion():
		print("Podemos agregar codigo antes")
		funcion()
		print("Podemos agregar codigo despues")
		
	return nueva_funcion

@decorador
def funcion_a_decorar():
	print("Esta es una funcion a decorar")

funcion_a_decorar()









