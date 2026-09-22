"""
Escribir un programa que calcule la suma de los
num naturales.
Por ejem si n=100, el programa calculara la suma 
del 1 al 100
"""
# Importamos biblioteca time
import time

#Creando una marca de tiempo
timestamp_01 = time.time()

#Programa que calcula la suma de los "n" num 
#naturales
n=100
total_Sum=0

#Ciclo for
for number in range(1,n+1):
    total_Sum = total_Sum + number
    #1) sum <- 0 +´1
    #Sum = 1
    #2) Sum <- 1 + 2
    #Sum = 3
    #...
    #100) Sum <- Sum_(-1) + 100
print(f"La suma de 1 hasta {n} es: {total_Sum}")
#f = Formato

timestamp_02 = time.time()

#Impresion del tiempo de ejecucion
print(f"Tiempo de ejecucion:{((timestamp_02 - timestamp_01)*1e6):.2f} μs")