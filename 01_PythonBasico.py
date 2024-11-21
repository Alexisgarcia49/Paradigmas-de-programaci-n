#==============================
# Alexis García
#==============================
# Paradigmas de Programación
# Matemática Algorítimica
# ESFM IPN Sept-2025
#==============================

''' ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
'''

#=====================
# Operaciones básicas
#=====================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5) # Raíz cuadrada
print (10%2)
print (10%0.1) # Exclusivo de python

#===========================================
# Para saber el tipo de objeto se usa type
#===========================================

t= 0
print(type(t)) # entero
t = 3.6
print(type(t)) # real (flotante)
t= True
print(type(t)) # booleano (bool)

#======================
# Mensajes a pantalla
#======================
print ("Este es un comando de python. ", "Este es otro enunciado.",t)
print('id: ', 1)
print('Nombres: ', 'Steve')
print('Apellidos: ','Jobs')
print("Vamos a sumar esto" + " con esto otro")

#================================================
# Continuar una instrucción en varios renglones
#================================================
if 100 > 99 and \
	200 <= 300 and \
	True != False:
		print('¡Hola a todos!')

#=========================================
# Comandos diferentes en la misma línea
#=========================================
print('Hola '); print('tu') # Se considera mala práctica

#==================================================
# Usando paréntesis redondos, cuadrados o llaves
# se puede escribir en varios renglones
#==================================================
lista = [ 1, 2, 3, 4,
	5, 6, 7, 8,
	9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(lista)
print(matriz)

#===================================================================
# Indentación estricta para procesos depedientes de : (dos puntos)
#===================================================================
if 10>5:
	print("Dies es mayor que cinco")
	print("otra indentación")
for i in lista:
	print (i)
	print('ok')
if 10>5:
	print("verdadero")
	if 10<20:
		print("verdadero")
elif 5>3: # Comienza segundo condicional
	print ('esto no se imprimirá')
else:
	print('Aquí nunca llega')

#============
# Funciones
#============
def saludar(nombre):
	print('Hola ', nombre)
	print(" bienvenidos al tutorial de python")

saludar ("Alexis")
