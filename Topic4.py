class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        nodes = []
        if self.head:
            temp = self.head
            while True:
                nodes.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        return nodes


orders = CircularLinkedList()
for order in ["Order 1", "Order 2", "Order 3"]:
    orders.append(order)
print("Circular Linked List Orders:", orders.display())