#from array import *
#Ó
import array as arr

#Creacion de arreglo
# 1: Entero con signo
# 2: Entero sin signo
# 3: Num decimal
# 4: Num decimal doble
# 5: Caracteres unicode
my_array = arr.array('i',[10,22,300,6,10,800,64,67,8,90,100])
#Interacion automatica
#for num in my_array:
    #print(num)

#Accesoo individual a los elementos
#print(my_array[0]) #Primer elemento
#print(my_array[1]) #Segundo elemento
#print(my_array[1]) #Tercer elemento

#Tamaño de arreglo
#Length
#print(len(my_array))

#Interacion por indices
for i in range(len(my_array)):
    if my_array[i] % 2 == 0:
        print(f"Elemento Num {i+1}: {my_array[i]}")
    

