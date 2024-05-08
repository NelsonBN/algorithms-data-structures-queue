class Queue: # O(n) -> space complexity
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0


    def enqueue(self, item): # O(1) -> Time complexity
        if self.size == self.capacity:
            raise Exception("Queue is full")
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1


    def dequeue(self): # O(1) -> Time complexity
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.queue[self.head]
        self.queue[self.head] = None  # Optional: Clear the slot for garbage collection
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item


    def peek(self): # O(1) -> Time complexity
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.head]


    def is_empty(self): # O(1) -> Time complexity
        return self.size == 0


    def is_full(self): # O(1) -> Time complexity
        return self.size == self.capacity



queue = Queue(5)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f'dequeue -> {queue.dequeue()}')   # Output: 10
print(f'peek -> {queue.peek()}')         # Output: 20
print(f'is_empty -> {queue.is_empty()}') # Output: False

queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

print(f'is_full -> {queue.is_full()}') # Output: True
print(f'dequeue -> {queue.dequeue()}') # Output: 20
print(f'dequeue -> {queue.dequeue()}') # Output: 30
print(f'dequeue -> {queue.dequeue()}') # Output: 40
print(f'dequeue -> {queue.dequeue()}') # Output: 50
print(f'dequeue -> {queue.dequeue()}') # Output: 60
