from typing import Final

@final
class a:
    def __init__(self):
        self.name="CA"
        self.sclass="1"


class g(a):
    def __init__(self):
        self.name="sa"
        self.sclass="12"

f=a()
x=g()
class inn:
    name : Final[str]="dsad"
    name = "fafsaf"
    def __init__(self,name,age=0):
        self.name=name
        self.age=age

v=inn("das")
print(v.name,inn.name )

for i in range(0,12):
    print(i)
    if i == 3:
        break
else:
    print("done")

try:
    f=100/0

except ZeroDivisionError:
    print("error")
else:
    print("fff")
finally:
    print("hhhh")

from collections import  deque
c=deque([1,2,3,4,5])
c.rotate(2)
for i in range(len(c)):
    print(c.pop())

import pdfminer.six as px
f=px()
