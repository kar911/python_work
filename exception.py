import sys
def d():
    print("s")
    return 's1'
# assert ('linux' in sys.platform),d()
assert ('a'<'b'),d()
x = int(input(":"))
if x >10:
    raise Exception('x should not exceed 5. The value of x {}was: '.format(x))
