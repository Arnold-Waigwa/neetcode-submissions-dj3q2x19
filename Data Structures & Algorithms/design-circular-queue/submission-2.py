class MyCircularQueue:

    def __init__(self, k: int):
        self.array = [0] * k
        self.capacity = k
        self.count = 0
        self.head, self.tail = 0, 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.array[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.array[self.head]

        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            if self.tail == 0:
                return self.array[self.tail + self.capacity - 1]
            else:
                return self.array[self.tail - 1]     

        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()