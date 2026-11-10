# Despues de la clase generators
class Node:
  #Constructor
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def iter(self):
        current = self
        while current: 
            value = current.data
            current = current.next
            yield value 

# Creando una funcion principal
def main ():

# Testear la clase nodo
    Node_01 = Node("eggs")
    Node_02 = Node("ham")
    Node_03 = Node("bacon")

# print("🖇NODES SIN ENLAZAR🖇")
# print(f"Node 01: D:{Node_01.data}")
# print(f"Node 02: D:{Node_02.data}")
# print(f"Node 03: D:{Node_03.data}")
   
    print ("NODES")
    print (f"Node 01: D: {Node_01.data} - N: {Node_01.next}")
    print (f"Node 02: D: {Node_02.data} - N: {Node_02.next}")
    print (f"Node 03: D: {Node_03.data} - N: {Node_03.next}")

#Enlasando los nodos
    Node_01.next = Node_02
    Node_02.next = Node_03

    print("🖇NODES ENLAZADOS🖇")
    print(f"Node 01: D:{Node_01.data} - N: {Node_01.next}")
    print(f"Node 02: D:{Node_02.data} - N: {Node_02.next}")
    print(f"Node 03: D:{Node_03.data} - N: {Node_03.next}")

# List Traversal (Recorrido de la lista)
    current = Node_01
    while current:
        print(current.data, end="-->")
        current = current.next
    print(" ")
     
    for Node_value in Node_01.iter():
        print (Node_value) 

#Invocando a Main
if __name__ == "__main__":
    main()