#====================================
# Alexis García
#====================================
# Matemática Algorítmica
# ESFM IPN
# Septiembre de 2024
#====================================

#============================================================
# Input permite obtener datos del usuario en prompter
#============================================================
nombre = input("Dame tu nombre: ") 
print("Hola como estás",nombre)

#========================================
# Los enteros son de precisión ilimitada
#========================================
y = 50000000000000000000000000000000000
print (y)

#===============================================================
# Se pueden delimitar números con guión bajo, pero no con coma
#===============================================================
y = 5_000_000
print(y)

#======================================================
# La función int () cambia strings y floats a enteros
#======================================================
numero = int(input("Dame tu edad: "))
type(numero)

#=====================================================
# La notación científica de flotantes utiliza e ó E
#=====================================================
# 1.2 x 10^{-9}
#===============
y = 1.2E-09
print (y)

#==========================================================
# La función float() convierte strings y enteros a floats 
#==========================================================
y = float ("14.3")
print(y)

#==========================================================
# Los complejos se escriben con la raíz de menos uno
# j siempre como un número como prefijo
# no acepta la j suelta
#==========================================================
z = 1+1j
print(z)


# Suma +
# Resta -
# Multiplicaión *
# División -
# Módulo %
# Exponente **
# // Función piso
# Funciones para transformar números int () float() complex()
# Operaciones abs() round() pow()

print(round(3.1415,4))

#==========================
# String de varias líneas
#==========================
parrafo = """ En el bosque de la china
la chinita se perdión"""
print(parrafo)

#==================================================
# La función len() obtiene el tamaño del string
#==================================================
n = len(parrafo)
print(n)

#===============================================================
# Las letras en un string ocupan lugares como un arreglo
# (también de atrás para adelante comenzando en -1 el último)
#===============================================================
palabra = "hola"
print(palabra[0])
print(palabra[-4])


