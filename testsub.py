import sys as s, os

# print(s.path)
print(s.modules.values())
print(os.name)
print(len(os.environ))
print(repr(os.linesep))
print(os.getcwd())
print(os.name)
print(os.uname())
os.spawnv(""," py1.py",[-2])
print(os.getpgid(1))
print(os.geteuid())
print(os.getegid())
print(os.getppid())
print(os.getpid())

# s={"a":{"b":"c","d":"f"}}
b = [i for i in reversed(range(10))]
l = iter(b)  # iter gives the iterable for b
for v in s["a"].values():
    print(v)
from  array import *
ar=array('i',[1,9,2,8,3,7,4,5,6])
for i in ar:
    print(i)
f=sorted(ar)
for i in f:
    print(i)
print(next(l))
print(next(l))
print(next(l))
# print(copyright())
print(repr("\n"))
print(round(124.3434, 2))
print(hash("dsadafs"))
print(hash("dsadafs"))
print(hex(id(l)))


class f():
    def fk(self):
        print("fk")


class f1(f):
    def __int__(self, d, g):
        self._d = d  # there is no specifier in python just to follow rules
        self._g = g

    def fkd(self):
        print("fk")

    @staticmethod
    def l():
        print("dsd")

    @property
    def d(self):
        print("d getter")
        return self._d

    @d.setter
    def d(self, value):
        print("d setter")
        if (value > 0):
            self._d = value

    @property
    def g(self):
        print("g getter")
        return self._g

    @g.setter
    def g(self, value):
        print("g setter")
        self._g = value


ds = f1()
# print(type.mro(ds)) # it show the serrise of class it belong to first it is f1 then f then a object
ds.g = 12
# print(ds.mro())# works same
d = [1, 2, 33, 3, 3, 3]
print(d.count(3))
print(ds._g)  # it will give direct access of _g
print(ds.g)  # it will give no direct access of g but can be checked
ds._d = 12  # it will give direct access of _g
ds._g = 14  # it will give direct access of _d
ds.d = -12  # it will give no direct access of d but can be checked -ve is not allowed
ds.g = 12  # it will give no direct access of g but can be checked
print(ds.d)

# immutable can have shared refferences
a=14
b=14
n=14
print(hex(id(a)),hex(id(b)),hex(id(n)))
# while mutables have no shared refferences while hac=ve same no shareing refeerence
o=[1,2,3]
p=[1,2,3]
print(hex(id(o)),hex(id(p)))
# diff btwen is and ==
print(o is p) # it is look for refference false
print(o == p) #it look for data true as same data

# None is a area like nullptr in c++ is object

# python  optimization
# interning is reusing object on demand
# auto interning in interger is in range -5 to 256
a=14 #works
b=14
n=14
#
a=1000000000 # is working
b=1000000000
print( a is b ,f" -> {a} {b}")
print(id(a),'-\n',id(b))
# auto interning in string is in can have normal look like identifire
# force intern can be done using sys.intern()
h="nnknkakdnsnansd nsndksandnsadnskddnasj dnasjnd"
j="nnknkakdnsnansd nsndksandnsadnskddnasj dnasjnd"
print(h is j)
print(id(h))
print(id(j))
# auto interning in tuple is in  len(T)<20
if d in [1,2,3,4]: # in this [1,2,3,4] eill be cover to tuple as constant
    pass
# set convert to frozzen set
b= 12 * 49 # is also const exp
b1= 12 * 49 #
print(b is b1) #thrugh
def func(e):
    i = 1212
    g = 1212
    m = [1,2,3,4]
print(func.__code__.co_consts) # gives list of const in a function

# sets are faster for comparision stuff