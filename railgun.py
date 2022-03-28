def a():
    print("a")
def b():
    print("b")
def c():
    print("c")
d = [b, a, c]
for i in range(3):
    d[i]()
