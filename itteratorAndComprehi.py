a=[1,2,4,5]
s=a[::-1]
d="adasdasdasaddsasassad"
print(d.split("d",6))
print(a[::-1])
sd=[a+2 for a in s if a%2==0 and a > 3]
print(sd)
print(s)

def v(**kwargs):
    print(f"{kwargs}")
    print("sas","dasdsa","dasd",sep=" < > ",end=" d",flush=True)

v(a=12,b=212,c=21)