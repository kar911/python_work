a=[]
for i in range(1,10):
    a.append(i)
print(a)
a.pop()
print(a)
class que:
    def __init__(self):
        self.q=[]
    def enq(self,data):
        self.q.append(data)
    def deq(self):
        s=self.q[0]
        del self.q[0]
        return s

s=que()
s.enq(12)
s.enq(13)
s.enq(14)
s.enq(15)
s.enq(16)
print(s.q)
s.deq()
s.deq()
print(s.q)


#  other of queue
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Queue:
    def __init__(self):
        self.tail=None
        self.head=None
        self.size=0
    def enq(self,data):
        self.size+=1
        new=Node(data)
        if self.tail is None:
            self.tail=new
        elif self.tail.prev is None:
            self.head=new
            self.tail.prev=new
            new.next=self.tail
        else:
            nex=self.head
            self.head = new
            new.next = nex


    def deq(self):
        if self.tail is None:
            print("no element left in queue")
        else:
            self.size-=1
            if self.head.next is self.tail:
                self.tail=self.head
                self.head=None
            elif self.tail.prev is None:
                self.tail=None
            else:
                self.tail=self.tail.prev

    def trev(self):
        d=self.size
        c=self.head
        while d > 0:
            print(c.data)
            c=c.next
            d-=1

l=Queue()
l.enq(12)
l.enq(13)
l.enq(14)
l.enq(15)
l.enq(16)
l.enq(17)
print(l.size)
l.deq()
l.deq()
l.deq()
l.trev()
print(l.size)
