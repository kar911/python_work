def prime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")

def alprime(lower=0,upper=10): #print all prime upto
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num,",",end=" ")
    else:
        print(end="\n")
#factorial of number
def facto(num,factorial=1):
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
        return None
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial
#palindrome or not
def pelind(n):
    temp=n
    rev = 0
    while (n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if (temp == rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
#angstrom or not
def angstrom(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

#find the total number of digits in the number
def numcoutshow(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    print("total number"+count)

#find the total number of digits in the number
def numcoutret(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count

#decimal to binar
def dtoB(num):
    return "{0:b}".format(num)
#decimal to octnum
def dtoO(num):
    return "{0:o}".format(num)
#decimal to hexadecimal
def dtoX(num):
    return "{0:x}".format(num)

#octal to binary return
def OToBret(octnum):
    binary = ""
    while octnum != 0:
        # extracting each digit
        d = int(octnum % 10)
        if d == 0:
            # concatination of string using join function
            binary = "".join(["000", binary])
        elif d == 1:
            # concatination of string using join function
            binary = "".join(["001", binary])
        elif d == 2:
            # concatination of string using join function
            binary = "".join(["010", binary])
        elif d == 3:
            # concatination of string using join function
            binary = "".join(["011", binary])
        elif d == 4:
            # concatination of string using join function
            binary = "".join(["100", binary])
        elif d == 5:
            # concatination of string using join function
            binary = "".join(["101", binary])
        elif d == 6:
            # concatination of string using join function
            binary = "".join(["110", binary])
        elif d == 7:
           # concatination of string using join function
            binary = "".join(["111", binary])
        else:
            # an option for invalid input
            binary = "Invalid Octal Digit"
            break
        # updating the oct for while loop
        octnum = int(octnum / 10)
        # returning the string binary that stores
    return binary

#to count the number of time a digit apears in number
def numcoutspec(n,d):
    count=0
    while(n>0):
        if n % 10 ==d:
            count=count+1
        n=n//10
    return count

#find the number of time a digit apears in a number contigusly max
def streak(n,d):
    count = 0
    m=[0,0]
    while (n > 0):
        if n % 10 == d:
            count = count + 1
            if max(m) < count:
                if len(m) != 1:
                    m.pop()
                m.append(count)
        else:
            count=0
        n = n // 10
    return m[1]

#give streak count,last position,first position
def streakends(n,d):
    count = 0
    m ={0:0}
    i=0
    while (n > 0):
        if n % 10 == d:
            count = count + 1
            if max(m.keys()) < count:
                if len(m) != 1:
                    m.clear()
                e=i
                x={count:[e+1,e-count+2]}
                m.update(x)
        else:
            count = 0
        n = n // 10
        i = i + 1
    return max(m.keys()),max(m.values())[0],max(m.values())[1]

#it extractle the sub digits from a number
def extractle(nl,le,w):
    n=int(rev(nl))
    n=round(n,-le)
    for i in range(0,le):
        n=n//10
    o=[]
    while n>0 :
        s=n%(pow(10,w))
        o.append(int(rev(s)))
        n=n//(pow(10,(le+w)))
    return o

def extractw(nl, le, w):
    n = int(rev(nl))
    o = []
    while n > 0:
        s = n % (pow(10, w))
        o.append(int(rev(s)))
        n = n // (pow(10, (le + w)))
    return o

def rev(n):
    nl=n
    c=0
    while nl>0:
        c=c+1
        nl=nl//10
    s=0
    if n%10==0 :
        n=n*10+1
    while(n>0):
        s=s+((n%10)*pow(10,c-1))
        n=n//10
        c=c-1
    return s

def oto2(n):
    s=0
    i=0
    while n>0:
       p=n%10
       if p == 0:
           p=2
           s=s+(p*pow(10,i))
       else:
           s=s+(p*pow(10,i))
       n=n//10
       i = i + 1
    return s

def t2to(n):
    s=0
    i=0
    while n>0:
       p=n%10
       if p == 2:
           p=0
           s=s+(p*pow(10,i))
       else:
           s=s+(p*pow(10,i))
       n=n//10
       i = i + 1
    return s

def extractle2(nl,le,w):
    n=oto2(nl)
    n=int(rev(n))
    n=round(n,-le)
    for i in range(0,le):
        n=n//10
    o=[]
    while n>0 :
        if (n < 99):
            s = n % (pow(10, w))
            if s == 12:
                s = 212
                o.append(t2to(int(rev(s))))
            elif s == 1:
                s = 221
                o.append(t2to(int(rev(s))))
            elif s == 21:
                s = 221
                o.append(t2to(int(rev(s))))
            else:
                o.append(t2to(int(rev(s))))
        else:
            s=n%(pow(10,w))
            o.append(t2to(int(rev(s))))
        n=n//(pow(10,(le+w)))
    return o


def extractw2(nl, le, w):
    n=oto2(nl)
    n = int(rev(n))
    o = []
    while n > 0:
        if(n < 99):
            s = n % (pow(10, w))
            if s==12:
                s=212
                o.append(t2to(int(rev(s))))
            elif s==1:
                s=221
                o.append(t2to(int(rev(s))))
            elif s==21:
                s=221
                o.append(t2to(int(rev(s))))
            else:
                o.append(t2to(int(rev(s))))
        else:
            s = n % (pow(10, w))
            o.append(t2to(int(rev(s))))
        n = n // (pow(10, (le + w)))
    return o

def bindiv(d,n):
    if type(d) == str and type(n) == str:
        d = int(d, 2)
        n = int(n, 2)
    else:
        d = int(f"{d}", 2)
        n = int(f"{n}", 2)
    c=d//n
    return bin(c)

def binmul(d,n):
    if type(d) == str and type(n) == str:
        d = int(d, 2)
        n = int(n, 2)
    else:
        d = int(f"{d}", 2)
        n = int(f"{n}", 2)
    c = d * n
    return bin(c)
