 def a1():
     print("Hello WORLD!")
 a1()

 def a2():
     print("the sum of the two numbers is : ",int(input("enter the first number >"))+int(input("enter the second number >")))
 a2()
 def a3():
     import math
     print("the square root of the number is : ", math.sqrt(int(input("enter the number to find square root  >"))))
 a3()
 def a4():
     print("the area of the triangle is : ",0.5*int(input("enter the height of the triangle >"))*int(input("enter the base of the triangle >")))
 a4()
 def a5():
     print("ax^2 +bx+c")
     a=int(input("enter the value of a >"))
     b= int(input("enter the value of b >"))
     c= int(input("enter the value of c >"))
     import math
     try:
         print("the solution of the given quadratic equation is",(-b+(math.sqrt((b*b)-(4*a*c))))/(a*2),(-b-(math.sqrt((b*b)-(4*a*c))))/(a*2))
     except ValueError as d:
         print("problem in your input" ,d)
     except ZeroDivisionError as d:
         print("problem in your input" ,d)
 a5()
 def a6():
     a = int(input("ENTER a >"))
     b = int(input("ENTER b >"))
     a=a+b
     b=a-b
     a=a-b
     print(f"after swap a={a} b={b}")
 a6()
 def a7():
     import random
     print("the random generated number is b/w 1-10 >",random.randint(1,10))
 a7()
 def a8():
     print(f"conversion to miles {1.60934*int(input('the value in kilometer >'))}")
 a8()
 def a9():
     print(f"conversion to Fahrenheit {1.8*int(input('enter the temperature in degree Celsius>'))+32}")
 a9()
 def a10():
     import re
     x=int(input("enter a number >"))
     if x < 0:
         print("its -ve")
     elif x > 0:
         print("its +ve")
     else:
         print("its zero")
 a10()
 def a11():
     if int(input("to check for Even no enter number >"))%2==0:
         return True
     return False
 print(a11())
 def a12():
     x=int(input(" is leap or not year enter the year >"))
     if x%400==0:
         print("leap")
     elif x%100==0:
         print("not leap")
     elif x%4==0:
         print("leap")
     else:
         print("not leap")
 a12()
 def a13():
     print("the maximum number is ",max(int(input("no.1>")),int(input("no.2>")),int(input("no.3>"))))
 a13()
 def a14():
     num=int(input("to check for prime enter number >"))
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
 a14()
 def a15():
     print("prime numbers in between 0 to 100")
     lower = 0
     upper = 100
     for num in range(lower, upper + 1):
         # all prime numbers are greater than 1
         if num > 1:
             for i in range(2, num):
                 if (num % i) == 0:
                     break
             else:
                 print(num,end=",")
     else:
         print(end="\n")
 a15()
 def a16():
     num=int(input("enter number to find its factorial >"))
     factorial = 1
     if num < 0:
         print("Sorry, factorial does not exist for negative numbers")
     elif num == 0:
         print("The factorial of 0 is 1")
     else:
         for i in range(1, num + 1):
             factorial = factorial * i
         print(factorial)
 a16()
 def a17():
     num = int(input("enter the number for table >"))
     if num > 0:
         for i in range(1,11):
             print(i*num)
 a17()


 # def a18():
 # # 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
 # # febnachi to 20   watch for the non prime in below goo pattern
 # # 0,1,1,2,4,7,11,16,22,29,37,46,56,67,79,92,106,121,137,154,172,191,
 #     print("febnachi to 20")
 #     next=1
 #     print("0,",end="")
 #     for i in range(0,21):
 #         print(next,end=",")
 #         nth=i+next
 #         next=nth
 def a18():
     print("Fibonacci to 20")
     n1,n2=0,1
     print("0,",end="")
     for i in range(0,21):
         print(n1,end=",")
         nth=n1+n2
         n1=n2
         n2=nth
     print(" ")
 a18()
 def a19():
     print("Sentence with understandable semantics but incorrect syntax >",f"cow give{'s'.upper()} milk")
     print("Sentence with correct syntax but semantic errors >","cow takes milk")
 a19()
 def a20():
     import time
     num=20
     try:
         for i in range(0,21):
             print(f"fuel {num}gal or {num*3.7854}L")
             num-=1
             time.sleep(1)
             if i ==6:
                 raise KeyboardInterrupt
     except KeyboardInterrupt:
         print("you stoped the car")
     else:
         print("no gas left!")
 a20()

 def a21():
     nam1 = str(input("enter your first favourite food >"))
     nam2 = str(input("enter your second favourite food >"))
     print("name of a new food by joining the original food names",nam1 + nam2)
 a21()
 def a22():
     bill=int(input("enter the amount of restaurant bill >"))
     return f"15% Tip Will Be > {bill+(bill*(15/100))}\n20% Tip Will Be > {bill+(bill*(20/100))}"
 print(a22())
 def a24():
     num = int(input("enter the radius of circle>"))
     import math
     return pow(num, 2) * math.pi
 print("area of circle is ",a24())
 def mysum(*args):
     print(args)
     return sum(args)
 print(mysum(21,84,67))

 class d:
     def __init__(self,name,age):
         self.name=name
         self.age=age
     def __add__(self, other):
         return self.name+other.name,self.age+other.age
 dd=d("kar",12)
 d2=d("tik",13)
 df=dd+d2
 print(df)

def a23():
    nam1 = int(input("base prize of car>"))
    tax,license=(nam1*1)/100,(nam1*1)/100
    dp=10
    dsc=20
    print("total costing(on road pricing) of the car",nam1+tax+license+dp+dsc)
 a23()

 feb1()
 # feb()
 f1=[]
 def a18():
     # print("Fibonacci to 20")
     n1,n2=0,1
     # print("0,",end="")
     for i in range(0,301):
         f1.append(n1)
         nth=n1+n2
         n1=n2
         n2=nth
 a18()
 # print(f1[2:] == f)
 f1.remove(0)
 f1.remove(1)
 for i in range(len(f)):
     print(f1[i] == f[i])
def a15():
    print("prime numbers in between 0 to 100")
    lower = 0
    upper = 100
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num,end=",")
    else:
        print(end="\n")

