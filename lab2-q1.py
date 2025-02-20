class Stack:
    def __init__(self):
        self.top = -1
        # this stack is implemented with Python list (array)
        self.data = []

    def push(self, value):
        self.data.append(0)
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        value = self.data[self.top]
        # delete the top value using del
        del self.data[self.top]
        self.top -= 1
        return value
    
    def isEmpty(self):
        return (self.top == -1)
    
    def peek(self):
        pass

    def printStack(self):
        print(self.data)

    def invert(self):
        tempStack = Stack() # assign a new temp Stack object
        while self.isEmpty() is False: # while the Stack is not empty
            tempStack.push(self.pop())
        self.data = tempStack.data
        self.top = tempStack.top

s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.printStack()
s.invert()
s.printStack()

# invert method for stack