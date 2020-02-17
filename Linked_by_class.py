class node:
    def __init__(self,data):
        self.data = data  
        self.next = None

class linkedlist(node):
    
    def __init__(self):
        self.head=None

    def insert(self,data):
        if(self.head==None):
            self.head=node(data)
        else:
            new=node(data)
            c=self.head
            while(c.next):
                c=c.next
            c.next=new

    def display(self):
        c = self.head
        while(c.next):
            print(c.data)
            c=c.next
        print(c.data)

l = linkedlist()
l.insert(10)
l.insert(20)
l.insert(30)
l.display()