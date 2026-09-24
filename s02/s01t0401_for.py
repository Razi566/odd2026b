"""
Escribir un programa que calcule la suma de los
num naturales.
Por ejem si n=100, el programa calculara la suma 
del 1 al 100
"""
# Importamos biblioteca time
import time
def Sum_of_n(n):
  total_Sum=0
  #Sumando los n num
  #Ciclo for
  for number in range(1,n+1):
    total_Sum = total_Sum + number
  #Retornando el total de la suma
  return total_Sum

#Variable para guardar
#El data set
dataset = [] #[(n,time,sum),(n,time,sum)]

#Generando el contenido del Dataset
for repetition in range(1,11):
  #⌛Tomo el tiempo 1
  #Creando una marca de tiempo
  timestamp_01 = time.time()
  #Sumo los n Numeros
  n = repetition*500
  #Guardar el resultado en memoria
  result = Sum_of_n(n)
  #Tomando el tiempo final
  timestamp_02 = time.time()

  #Calculando el tiempo final
  elapsed_time = round((timestamp_02 - timestamp_01)*1e6,2)

  #Agregar la tripleta de los datos al data set
  dataset.append( (n,elapsed_time,result) )

#Imprimir el dataset
for tup in dataset:
    print(tup)

