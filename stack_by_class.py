class Stack():
    def __init__(self):
        self.list_values=[]

    def push(self,element):
        self.list_values.append(element)

    def pop(self):
        return self.list_values.pop()

    def display(self):
        print(self.list_values)

m = Stack()
m.push(20)
m.push(30)
m.display()
print(m.pop())
m.display()