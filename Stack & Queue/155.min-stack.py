class MinStack():

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if len(self.min_stack) == 0 or val < self.stack[self.min_stack[-1]]:
            self.min_stack.append(len(self.stack) - 1)
            

    def pop(self):
        self.stack.pop()
        if len(self.min_stack) > 0 and self.min_stack[-1] == len(self.stack):
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.stack[self.min_stack[-1]]
    
minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(0)

print(minStack.getMin())
minStack.pop()
minStack.pop()
print(minStack.getMin())