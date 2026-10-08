"""
Escribir un programa que calcule la suma de los
num naturales.
Por ejem si n=100, el programa calculara la suma 
del 1 al 100
42 usando un ciclo while
"""
# Importamos biblioteca time
import time
n = 100
the_sum = 0
#⌛Tomo el tiempo 1
#Creando una marca de tiempo
timestamp_01 = time.time()

#Iniciando la suma 
while(n > 0):
   the_sum = the_sum + n # 100 + 99 + 98 + ... + 1
   n = n - 1
#Tomando el tiempo 2
timestamp_02 = time.time()

#Imprimimos la solucion 
print(f"La suma es {the_sum}")

#Calculando el tiempo 
elapsed_time = round((timestamp_02-timestamp_01)*1e6,2)
print(f"Tiempo de ejecucion: {elapsed_time}μs")



