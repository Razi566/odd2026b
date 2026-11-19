# Importando clase Node
from s02t0201_Linked_list import Node

# Creando la clase de una lista enlazada
class SinglyLinkedList:
    # Constructor 
    def __init__(self):
        self.head = None
    # Metodo de insercion de Nodo en la lista
    def append(self, data):
        # Creo el nodo 
        new_node = Node(data)
        # Si la lista esta vacia,
        # apuntamos el head al nuevo nodo que se creo
        if not self.head:
            self.head = new_node
            return
        # Si la lista no esta vacia, hay que recorrer el nodo
        # al final de la lista
        #Estableciendo el nodo actual como el primero de la lista
        Current_node = self.head
        while Current_node.next:
            Current_node = Current_node.next

        Current_node.next = new_node

# ! Creo funcion principal
def main():
    #Creando una instancia de una lista enlazada
    My_List = SinglyLinkedList()
    #Agregamos elementos de la lista
    My_List.append(30)
    My_List.append(59)
    My_List.append(80)
    My_List.append(100)

    #Recorrer la lista 
    for value in My_List.head.iter():
        print(f"{value},")

    # 2 Coloco el codigo en ejcutable
    #test_node = Node("Prueba")
    #print(f"Valor del nodo: {test_node.data}")

# Evaluo el valor de __name__
if __name__ == "__main__":
    main()