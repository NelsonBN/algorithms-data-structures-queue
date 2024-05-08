class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue: # O(n) -> space complexity
    def __init__(self):
        self.head = None
        self.tail = None


    def enqueue(self, item): # O(1) -> Time complexity
        node = Node(item)
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node


    def dequeue(self): # O(1) -> Time complexity
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value


    def peek(self): # O(1) -> Time complexity
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.value


    def is_empty(self): # O(1) -> Time complexity
        return not self.head



queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f'dequeue -> {queue.dequeue()}')   # Output: 10
print(f'peek -> {queue.peek()}')         # Output: 20
print(f'is_empty -> {queue.is_empty()}') # Output: False

queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

print(f'dequeue -> {queue.dequeue()}') # Output: 20
print(f'dequeue -> {queue.dequeue()}') # Output: 30
print(f'dequeue -> {queue.dequeue()}') # Output: 40
print(f'dequeue -> {queue.dequeue()}') # Output: 50
print(f'dequeue -> {queue.dequeue()}') # Output: 60
