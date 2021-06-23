#variables

# CONSTANTE = "Soy una constante"
#tutor = "Codi"
#print(tutor)
#print(CONSTANTE)
# Las constantes se ponen en mayúscula 


#Variables multi linea 

"""
valor_uno = 10
valor_dos = "Codi"
valor_tres = 10 * 20

valor_uno, valor_dos, valor_tres = 10,"Codi", 10*20
""" 

# Operadores relacionales y logicos 
"""
variable_uno = 10
variable_dos = 18

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)


resultado = True and True and diferente
print(resultado)
resultado_or = True or True or diferente
print(resultado_or)
resultado_not = True not True not diferente
print(resultado_not)
"""

# Entrada de datos por teclado 
nombre = input("Cual es tu nombre?\n")

edad = int(input("Cual es tu edad?\n"))

print("Cual es tu peso? ")
peso = float(input())

print("Estas autorizado? (si/no)")
autorizado = input() == "si"

print("Hola ", nombre)
print("Edad ", edad)
print("Peso ", peso)
print("Autorizado ",autorizado)




