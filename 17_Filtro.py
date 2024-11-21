#==============================
# Alexis García
#==============================
# Paradigmas de Programación
# Matemática Algorítmica
# ESFM IPN Octubre 2024
#==============================

#=================
# Uso de filtros
#=================

#========================================================= 
# Hacer una lista de los números por ariba del promedio
#=========================================================

# Módulo de estadística
import statistics

bigdata = [1.3,2.7,8.8,4.1,4.3,0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#=====================================================================
# Hazme una lista de elementos que cumplan la condición x > promedio
# filter( condicioón, datos)
#=====================================================================
print(list(filter(lambda x: x > promedio, bigdata)))

#====================
# Limpiar los datos
#====================
paises = ["", "Argentina", "", "Brasil", "", "Chile", "México", "", "Colombia", "", "", "Cuba", "Venezuela"]

#=================================
# Filtra lo que no contiene nada
#=================================
print(list(filter(None, paises)))
