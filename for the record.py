# import pandas as p
import numpy as n
for i in range(len(dir(n))):
    if i%10!=0:
        print(dir(n).pop(i),end=',\t')
    else:
        print(dir(n).pop(i),end="\n\n")

a=n.array([1,2,3,55])