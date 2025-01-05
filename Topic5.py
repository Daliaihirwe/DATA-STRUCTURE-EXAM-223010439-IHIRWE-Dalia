class Order:
    def __init__(self, order_id, customer_name, address):
        self.order_id = order_id
        self.customer_name = customer_name
        self.address = address

    def __str__(self):
        return f"Order[ID: {self.order_id}, Customer: {self.customer_name}, Address: {self.address}]"


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        for item in reversed(self.stack):
            print(item)


if __name__ == "__main__":

    order = Order("ORD123", "John Doe", "789 Elm St")

    
    tracking_stack = Stack()

    print("Tracking Order Events...")
    tracking_stack.push("Order Placed")
    tracking_stack.push("Order Packed")
    tracking_stack.push("Out for Delivery")
    tracking_stack.push("Delivered")

    print("\nCurrent Events in Stack (Top to Bottom):")
    tracking_stack.display()

    print("\nMost Recent Event:", tracking_stack.peek())

   
    print("\nPopping the Last Event:", tracking_stack.pop())
    print("\nUpdated Events in Stack (Top to Bottom):")
    tracking_stack.display()

    
    print("\nIs the Stack Empty?", tracking_stack.is_empty())
