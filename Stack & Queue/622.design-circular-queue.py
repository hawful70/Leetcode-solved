class MyCircularQueue():

    def __init__(self, k):
        self.queue = [0] * k
        self.front = -1
        self.rear = -1
        self.size = k
        

    def enQueue(self, value):
        if self.isFull():
            return False
        else:
            if self.front == self.rear == -1:
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

            return True
        

    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            if (self.front == self.rear):
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return True
        

    def Front(self):
        if self.front != -1:
            return self.queue[self.front]
        return -1

    def Rear(self):
        if self.rear != -1:
            return self.queue[self.rear]
        return -1        

    def isEmpty(self):
        if self.front == self.rear == -1:
            return True
        return False
        

    def isFull(self):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            return True
        return False
    
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1)) # return True
print(myCircularQueue.enQueue(2)) #return True
print(myCircularQueue.enQueue(3)) # return True
print(myCircularQueue.enQueue(4)) # return False
print(myCircularQueue.Rear())   # return 3
print(myCircularQueue.isFull())  # return True
print(myCircularQueue.deQueue()) # return True
print(myCircularQueue.enQueue(4)) # return True
print(myCircularQueue.Rear())   # return 4
