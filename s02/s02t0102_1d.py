#Importando el modulo array de la biblioteca array y renombrando como arr
from array import array as arr 

def print_array(input):
    print("[",end=" ")
    for element in input:
        print(element,end=',')
    print("]")

my_array = arr ('i',[2,10,15,20])
print_array(my_array)

#Buscar el elemeto 15
Number_to_search = 100
couter = 0
print(f"Se busca {Number_to_search} en el arreglo")
for integrer in my_array:
        if integrer == Number_to_search:
            print("Num encontrado")
            #Sirve para terminar el ciclo
            break
    #Incrementamos contador
        couter +=1
        if couter == len(my_array):
            print("Num NO encontrado")

