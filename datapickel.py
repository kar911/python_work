import pickle
d=[a for a in range(10) if a%2==0 ]
d1=[a for a in range(10) if a%2==0 ]
d2=[a for a in range(10) if a%2==0 ]
d4={k:v for k,v in [("dadsdas",2)] }
with open("data1.pickle",'wb') as f:
    pickle.dump((d,d1,d2,d4),f,pickle.HIGHEST_PROTOCOL)

with open("data1.pickle",'rb') as f:
    dd=pickle.load(f)

print(dd[0][::-1])
print(d4)
i,r=map(int,input().split())
print(i,r)

d=list( filter(lambda x: x>4 ,[12,42,3,1,10,11]) )
print(d)

print([-1,0,-3])

d=list( filter(lambda x: x>4 ,[12,42,3,1,10,11]) )
import typing
class ff:
    i=10

    def __init__(self):
        print("made")
    def gg(self):
        print("aggg")
    @staticmethod
    def g():
        print("static")
    @classmethod
    def h(cls):
        print("class")


print(ff.i)
print(ff.p)
ff.g()
g=ff()
ff.h()
print((1212.E100).as_integer_ratio())
v=(310).to_bytes(length=14,byteorder="little")
print(v)
print(int.from_bytes(v,byteorder="little"))
import array
class stack():
    def __init__(self,*arg):
        self.ele=array.array('b',*arg)
    def __repr__(self):
        for i in self.ele:
            print(i,end=',')
        return ""
    def push(self,num):
        self.ele.append(num)
    def popi(self):
        self.ele.pop()
    def top(self):
        return self.ele[-1]

s=stack([1,2,3,5,7,9,2,31,6])
s.push(34)
print(s.top())
s.push(24)
print(s.top())
# s.popi(24)
s.push(35)
print(s.top())
s.popi()
print(s.top())
s.popi()
print(s.top())
print(s)
s.popi(21)

import queue
d=queue.Queue(10)
for i in range(10):
    d.put(i)
print(d.get())
print(d.get())
print(d.get(block=True))
