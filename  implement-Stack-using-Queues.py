from collections import deque

class MyStack(object):
    def __init__(self):
        self.my_stack = deque()

    def push(self, x):
        self.my_stack.append(x)
        

    def pop(self):
        for i in range(len(self.my_stack) - 1):
            self.my_stack.append(self.my_stack.popleft())
        return self.my_stack.popleft()

    def top(self):
        return self.my_stack[-1]
        

    def empty(self):
        if len(self.my_stack) == 0:
            return True
        return False