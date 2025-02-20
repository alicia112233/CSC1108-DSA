class Stack:
    def __init__(self):
        self.top = -1
        # this stack is implemented with Python list (array)
        self.data = []

    def push(self, value):
        # increment the size of data using append()
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
        tempStack = Stack()
        while self.isEmpty() is False:
            tempStack.push(self.pop())
        self.data = tempStack.data

def checkBrace(s):
    myStack = Stack()
    for c in s:
        if c in ['(', '[', '{']:
            myStack.push(c)
        elif c in [")", "]", "}"]:
            if myStack.isEmpty():
                print("The string is not balanced")
                return
            else:
                c1 = myStack.pop()
                if (c == ")" and c1 != "(") or (c == "]" and c1 != "[") or (c
                == "}" and c1 != "{"):
                    print("The string is not balanced")
                    return
    if myStack.isEmpty() is False:
        print("The string is not balanced")
    else:
        print("The string is balanced")

checkBrace("{f(ff)}f[f]")

# a program that reads in a sequence of char and determines whether its parentheses, braces and curly brackets are balanced
# program needs to make sure that the grouping of symbols match up properly