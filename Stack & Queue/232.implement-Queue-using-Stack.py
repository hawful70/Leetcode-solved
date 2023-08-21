class MyQueue():

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)
        

    def pop(self):
        self.peek()
        return self.stack_out.pop()

    def peek(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
        

    def empty(self):
        if len(self.stack_in) == 0 and len(self.stack_out) == 0:
            return True
        return False