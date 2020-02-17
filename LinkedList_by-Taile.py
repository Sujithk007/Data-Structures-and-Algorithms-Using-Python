class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList(node):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,data):
        if(self.head==None):
            self.head = node(data)
            self.tail = self.head
        else:
            new = node(data)
            self.tail.next=new
            self.tail = self.tail.next

    def display(self):
        c=self.head
        t='['+str(c.data)
        c=c.next
        while(c.next):
            t=t+','+str(c.data)
            c=c.next
        t=t+','+ str(c.data)+']'
        print(t)

l = LinkedList()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.display()

