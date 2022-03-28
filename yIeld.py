import itertools
def fibonacci(i=10):
    a, b = 1, 1
    while i>0:
        yield a
        a, b ,i= b, a + b,i-1
f=fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f,"sorry"))

