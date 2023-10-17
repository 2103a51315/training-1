class node:
    def __init(self,val=0):
        self.prev=None
        self.val=val
        self.next=None
class doublell:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertAtbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            temp=node(data)
            temp.next=self.head
            self.head.prev=new
            self.head=temp
    def insertAtend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(data)
            curr.next=new
            new.prev=curr
            self.tail=new
    def deleteAtbeg(self):
        if self.head==None:
            return
        else:
            self.head=self.head.next
            self.head.prev=None
    def deleteAtend(self):
        if self.head==None:
            print("empty list")
        elif self.head.next==None:
            self.head=None
        else:
            prev=self.head
            curr=self.head.next
            while(curr.next):
                prev=curr
                curr=curr.next
            prev.next=None
            self.tail=prev
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end='->')
            temp=temp.next
        print(None)
l=[3,5,3,4,5]
o=doublell()
for i in l:
    o.insertAtend()
o.printing
o.insertAtbeg()
o.printing()
o.deleteAtbeg()
o.printing()
o.deleteAtend()
o.printing()
o.reverse()
o.printing()
    
        
            
    
            
        