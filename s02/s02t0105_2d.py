from array import array as arr

#Impresion de una tabla
def print_table(input_table):
#Imprimiendo cada elemento
 for row in Table:
    for Column in row:
        print(Column, end=",")
    print("\b ")

Table = [
    arr('i', [1,2,3]),
    arr('i', [4,5,6]),
    arr('i', [7,8,9]),
]

print_table(Table)   

#Insercion
row = 1
Column = 2
Value = 99

#Insertar en la fila 1 columna 2 el valor de 99
Table[row].insert(Column, Value)

#Imprimiendo mensaje
print("----DESPUES DE LA INSERCION----")
print_table(Table) #DRY

#Insertando una fila completa
new_row = arr('i', [100,200,300])
pos = 1
Table.insert(pos, new_row)

#Imprimiendo mensaje
print("----DESPUES DE LA INSERCION de la fila----")
print_table(Table) #DRY

#Eliminacion de fila
del Table[2]

#Imprimiendo mensaje 
print("----DESPUES DE LA ELIMINACION DE LA FILA 2----")
print_table(Table) #DRY