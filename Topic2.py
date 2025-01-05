from collections import deque

class Order:
    def __init__(self, order_id, customer_name, customer_address, priority):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.priority = priority

    def __str__(self):
        return f"OrderID: {self.order_id}, Customer: {self.customer_name}, Address: {self.customer_address}, Priority: {self.priority}"

class DeliveryQueue:
    def __init__(self):
        self.queue = deque()

    def add_order(self, order):
        self.queue.append(order)
        print(f"Order {order.order_id} added to the queue.")

    def process_order(self):
        if self.queue:
            order = self.queue.popleft()
            print(f"Processing {order}")
            return order
        else:
            print("No orders to process!")
            return None

    def show_orders(self):
        print("Orders in queue:")
        for order in self.queue:
            print(order)

class PriorityDeque:
    def __init__(self):
        self.deque = deque()

    def add_normal_order(self, order):
        self.deque.append(order)
        print(f"Normal order {order.order_id} added.")

    def add_priority_order(self, order):
        self.deque.appendleft(order)
        print(f"Priority order {order.order_id} added.")

    def process_order(self):
        if self.deque:
            order = self.deque.popleft()
            print(f"Processing {order}")
            return order
        else:
            print("No orders to process!")
            return None

    def show_orders(self):
        print("Orders in deque:")
        for order in self.deque:
            print(order)


order1 = Order("ORD001", "Alice", "123 Elm St", 1)
order2 = Order("ORD002", "Bob", "456 Pine Rd", 2)
priority_order = Order("ORD003", "Charlie", "789 Maple Ave", 1)
normal_order = Order("ORD004", "Diana", "321 Oak Blvd", 3)

priority_deque = PriorityDeque()
priority_deque.add_normal_order(normal_order)
priority_deque.add_priority_order(priority_order)
priority_deque.process_order()
priority_deque.show_orders()

delivery_queue = DeliveryQueue()
delivery_queue.add_order(order1)
delivery_queue.add_order(order2)
delivery_queue.process_order()
delivery_queue.show_orders()

