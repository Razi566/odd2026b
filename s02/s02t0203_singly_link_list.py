# Importando clase Node
from s02t0201_Linked_list import Node

# Creando la clase de una lista enlazada
class SinglyLinkedList:
    # Constructor 
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # Metodo de insercion de Nodo en la lista
    def append(self, data):
        # Creo el nodo 
        new_node = Node(data)
        #Si hay un tail el nuevo nodo pasa a ser el nuevo tail
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node

        # S ino hay un tail
        else:
            self.tail = new_node
            self.head = new_node
        # Se incrementa size en 1
        self.size += 1


        # Si la lista esta vacia,
        # apuntamos el head al nuevo nodo que se creo
        #if not self.head:
            #self.head = new_node
            #return
        # Si la lista no esta vacia, hay que recorrer el nodo
        # al final de la lista
        #Estableciendo el nodo actual como el primero de la lista
        # Current_node = self.head
        #while Current_node.next:
            #Current_node = Current_node.next

        #Current_node.next = new_node

    # Insertando en posicion media
    # [a ---> b ---> c] 0  4
    # [0  1  2]
    # size = 3
    def append_at_location(self, data, index):
        if index < 1 or index > self.size + 1:
            raise IndexError(f"Indice {index} fuera de rango")

        # Crear un nuevo nodo
        new_node = Node(data)

        # Insertar al inicio
        if index == 1:
            new_node.next = self.head
            self.head = new_node
            if self.tail == None:
                self.tail = new_node
            # Incremento en 1 el tamaño
            self.size += 1
        # Creando variables de control para las inserciones intermedias
        current = self.head
        prev = None
        Position = 1

        # Traversal (Recorrido)
        while current is not None and Position < index:
            prev = current
            current = current.next
            Position += 1
        # Llegando a la posicion
        if current is None:
            prev.next = new_node
            self.tail = new_node
            self.size += 1
            return

        # Si llegamos a una posicion intermedia
        # TODO: 

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