"""
#crear una clase 
class Usuario: 

	def __init__(self, username='', correo='', nombre=''):
		self.username = username
		self.correo = correo
		self.nombre = nombre

	def saluda(self): #todos deben llevar parametros
		return "Hola, soy un usuario " + self.nombre
	
	def mostrar_username(self):
		print(self.username)

	def mostrar_nombre(self):
		print(self.nombre)

codi = Usuario("Codi","codigofacilito@gmai.com","Codigo")
facilito = Usuario()

resultado = codi.saluda()
print(resultado)

print(type(codi)) # sbaer de cual clase es codi

codi.saluda("Codi")
facilito.saluda("Facilito")
"""

#Tipos de atributos
"""
class Circulo:
	pi = 3.14159265 # es una variable de case 
	def __init__(self, radio):
		self.radio = radio #es una variable de instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(circulo_a.pi)
print(circulo_b.radio)
"""

#metodos estaticos 
"""
class Triangulo:
	numero = 2
	@staticmethod
	def area(base, altura):
		return (base * altura) / Triangulo.numero


print(Triangulo.area(10,20))
"""

#metodos de clase
"""
class Circulo:
	pi = 3.14159265
	@classmethod
	def area(cls, radio): 
		return cls.pi * radio**2

print(Circulo.area(10))
"""

"""
#herencia
class Animal:
	def comer(self):
		print("Comiendo...")

	def dormir(self):
		print("Durmiendo...")

class Mascota:
	def fecha_adopcion(self, fecha):
		self.fecha_adopcion = fecha
		print(fecha)

class Perro(Animal, Mascota):
	def __init__(self, nombre):
		self.nombre = nombre

	def ladrar(self):
		print("Ladrando")

	def dormir(self):
		print(self.nombre, " esta durmiendo")
		Animal.dormir(self)
		print("No molestar")


class Gato(Animal):
	def ronronear(self):
		print("Ronronear")

firulais = Perro("Firulais")
firulais.dormir()
"""

"""
firulais.fecha_adopcion("Hoy")
firulais.ladrar()
firulais.comer()
firulais.dormir()
boladenieve = Gato()
boladenieve.dormir()
"""
# Sobre escribir métodos 
""" Volvemos a poner la funcion 
y ponemos el mensaje 
"""

# Clase Object 
class Gato:
	def __init__(self, nombre):
		self.nombre = nombre

	def __str__(self):
		return self.nombre

class Pato(object):
	def __init__(self, nombre):
		self.nombre = nombre

gato = Gato("Bigotes")
gato.edad = 6
pato = Pato("Luckas")

print(gato.__dict__)
print(pato)





