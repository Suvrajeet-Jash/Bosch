class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None  # Or raise exception

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None  # Or raise exception

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage:
q = Queue()

print("Enqueue elements: 10, 20, 30")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue size:", q.size())  # Output: 3
print("Peek:", q.peek())        # Output: 10

print("Dequeue:", q.dequeue())  # Output: 10
print("Dequeue:", q.dequeue())  # Output: 20

print("Is queue empty?", q.is_empty())  # Output: False

print("Dequeue:", q.dequeue())  # Output: 30

print("Is queue empty now?", q.is_empty())  # Output: True
print("Dequeue from empty queue:", q.dequeue())  # Output: None
