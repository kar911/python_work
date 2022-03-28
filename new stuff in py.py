#s="kartik"
# s={1:2,3:4,'h':'g'}
# for i,c in enumerate(s):# helps to index the s
#     print(i,c,s[c])
#
print("dadsa".center(10))

print("dscscs".count("scs"))
print("da   ff   gg".expandtabs(15))# no effect
print("da\tff\tgg".expandtabs(15))
print("da\tff\tgg".expandtabs())
print("dasd".maketrans({"a":1,"s":2,"d":3}))
print("kmdsmdkmd".replace("md","12"))
print("kmdsmdkmd".replace("md","12",2))
print("kmdkmdkmd".find("md"))
print("kmdkmdkmd".rfind("md"))
print("kmdkmdkmd".rindex("md"))
print("fasdsad fasfasf".title())
print("LOWER".lower())
print("upper".upper())
import string
c=type(False)
p1=[i for i in range(10)]
print(p1)
p1.pop(-1)
print(p1)
print(c.mro())

import array as ar
g=ar.array('b',(i for i in range(0,2)))
# g=ar.array('b',[0,1])
print(g.itemsize)
print(g)
g.append(41)
# g.byteswap()
print(g)
# g.byteswap()
print(g)
print(g.buffer_info())

import sys

print(sys.getsizeof(g))
#(140634853573296, 11)
print(140634853573296-139736798092928)
import time
strt=time.time()
g=ar.array('i',(i for i in range(0,1000)))
endd=time.time()
print(endd,strt,endd-strt,sep='\n')
0.00016379356384277344
strt=time.time()
g=ar.array('i',[i for i in range(0,1000)])
endd=time.time()
print(endd,strt,endd-strt,sep='\n')
0.0001533031463623047
strt=time.time()
g=ar.array('i',{i for i in range(0,1000)})
endd=time.time()
print(endd,strt,endd-strt,sep='\n')
0.0002079010009765625
print(min(0.0002079010009765625,0.0001533031463623047,0.00016379356384277344))