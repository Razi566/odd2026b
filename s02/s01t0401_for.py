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
Sum=0

#Ciclo for
for number in range(1,n+1):
    print(str(number) + " ")