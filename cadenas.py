"""
curso = "Curso de Python 3"
#otener cuantos valores hay en un string
resultado = len(curso)
#otener el valor de la letra 
resultado = curso[7]
print(resultado)
"""
#trabajo de string como listas
"""
lenguajes = "Python; Java; Ruby; PHP; Swift; Javascript; C#; C; C++"
separador = "; "
#separa el string en lista
resultado = lenguajes.split(separador)
#generar un string a partir de una lista 
nuevo_string = separador.join(resultado)
print(nuevo_string)
"""


#Formato de string 
"""
texto = " curso de python 3 python basico"
#generar la primera letra en mayuscula
resultado = texto.capitalize()
#generar el nuevo string de mayusculas a minusculas y viceversa
resultado = texto.swapcase()
#todas las letras a mayusculas
resultado = texto.upper()
#todas las letras a minusculas
resultado = texto.lower()
#formato con titulo 
resultado = texto.title()
#reemplazar un string por otro 
#cuando agregamos 1 es cuantos valores va a remplazar
resultado = texto.replace("python","java",1)
#retorna un string sin espacios  al principio y final
resultado = texto.strip()
print(resultado)

curso = "Python"
version = "3"
resultado = "Curso de %s %s" %(curso,version)
resultado = "Curso de {a} {b}".format(a=curso,b=version)
print(resultado)
print(f"Curso de {curso} {version}")
"""

#concatenacion
"""
curso = "Curso de Python"
curso = "c" + curso[1:] + " " + str(3) + " " + "en codigo facilito."
print(curso)
"""

#Saber si un string esta dentro de otro 
mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
resultado = mensaje.count("e")
#otra forma es 
resultado = "texto" in mensaje
#otra forma es pero arroja en que parte esta
resultado = mensaje.find("texto")
#extraer palabras
resultado = mensaje[resultado: resultado + len("texto")]
#saber si un string comienza con un mismo valor al igual que el final 
resultado = mensaje.startswith("Este")
#final 
resultado = mensaje.endswith("e")
print(resultado)