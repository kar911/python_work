"fa"
# from itertools import accumulate,permutations,product,starmap,combinations,combinations_with_replacement,filterfalse,takewhile,repeat
from itertools import *

a=[x for x in range(0,11)]
a.insert(3,41)
print(list(accumulate(a,lambda x,y: y-x)))
print(sum(a))
# print(next(itt.accumulate(a)))
# print(next(itt.accumulate(a)))
v=count(1,5)
c=cycle("DgSF")
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
f=[12,4,5,7,8]
print(list(compress('fregag',[1,0,1,0,1])))
print(list(dropwhile(lambda x: x<5,a))) # remove from starting until gets false then prints
# to remove all use
print(list(filterfalse(lambda x: x<6,a)))

##prime comprihension
a=[num for num in range(2,10) if all(num%j !=0 for j in range(2,num//2+1))]
print(a)
print(len(list(permutations([1,2,3,4,5],3))))
print(len(list(combinations([1,2,3,4,5],3))))
print(len(list(combinations_with_replacement([1,2,3,4,5],3))))
