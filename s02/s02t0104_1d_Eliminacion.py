from array import array as arr

#Importando una funcion de otro archivo
from s02t0102_1d import print_array

my_array = arr('i', [2, 10, 15, 20])

print("----ANTES DE LA ELIMINACION----")
print_array(my_array)

#Eliminacion
try:
    my_array.remove(100)
except:
    print(f"No se encuentra el arreglo baboso")
print("----DESPUES DE LA ELIMINACION----")
print_array(my_array)

