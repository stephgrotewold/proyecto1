class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, head):
        #Definir la cabeza de la Linked List
        self.head = head

    #Insertar un nuevo nodo
    def insert(self, data, position, ll):

        new_node = Node(data)
        if position == 0:
            new_node.next = ll.head
            ll.head = new_node
        else:
            current = ll.head
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node
    #Eliminar un nodo en la posición designada
    def delete(self, position):

            if position != 1:
                current = self.head
                k = 1
                while current.next is not None and k < position - 1:
                    current = current.next
                    k += 1
                if current.next is not None:
                    current.next = current.next.next
                    return True
                else:
                    return False
            else:
                self.head = self.head.next
                return True

     #Limpiar la LinkedList
    def deleteAllNodes(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None