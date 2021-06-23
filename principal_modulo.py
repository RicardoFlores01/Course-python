#Formas de importe 

#import modulos

#from modulos import * 
"""
Si queremos hacer este importe entonces 
para la funcion ponemos esto 
resultado = suma(5,10)
sin la palabra modulos antes de suma
"""

from modulos import suma as nueva_suma, resta

resultado = nueva_suma(5,10)
resultado1 = resta(5,10)
print(resultado)
print(resultado1)

# Archivos PYC
#Se creo una carpeta llamada pycache cuando trabajamos con modulos 
# Este archivo se crea pero ya compilado 
