class Order:
    def __init__(self, order_id, customer_name, address, priority):
        self.order_id = order_id
        self.customer_name = customer_name
        self.address = address
        self.priority = priority

    def __str__(self):
        return f"Order[ID: {self.order_id}, Customer: {self.customer_name}, Address: {self.address}, Priority: {self.priority}]"


class Node:
    def __init__(self, order):
        self.order = order
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, order):
        if not self.root:
            self.root = Node(order)
        else:
            self._insert_recursive(self.root, order)

    def _insert_recursive(self, current, order):
        if order.priority < current.order.priority:
            if current.left is None:
                current.left = Node(order)
            else:
                self._insert_recursive(current.left, order)
        elif order.priority > current.order.priority:
            if current.right is None:
                current.right = Node(order)
            else:
                self._insert_recursive(current.right, order)
        else:
            print(f"Duplicate priority {order.priority} detected! Ignoring order {order.order_id}.")

    def in_order_traversal(self):
        def traverse(node):
            if node:
                traverse(node.left)
                print(node.order)
                traverse(node.right)

        traverse(self.root)

if __name__ == "__main__":
    bst = BinarySearchTree()

    order1 = Order("ORD001", "Alice", "123 Maple St", 3)
    order2 = Order("ORD002", "Bob", "456 Oak St", 1)
    order3 = Order("ORD003", "Charlie", "789 Pine St", 5)
    order4 = Order("ORD004", "Diana", "321 Birch St", 4)
    order5 = Order("ORD005", "Eve", "147 Willow Ln", 2)

    bst.insert(order1)
    bst.insert(order2)
    bst.insert(order3)
    bst.insert(order4)
    bst.insert(order5)

    print("In-order Traversal of Orders (Sorted by Priority):")
    bst.in_order_traversal()
