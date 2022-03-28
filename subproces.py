import subprocess,sys

p1=subprocess.run('ls -la'.split(),capture_output=True)
print(p1.stdout.decode())
with open('tx1.txt','w') as f:
    p1=subprocess.run('ls -la'.split(),text=True,stdout=f)

p2=subprocess.run('cat txxt'.split(),capture_output=True,text=True)

p3=subprocess.run('grep -n  -i ads'.split(),capture_output=True,text=True,input=p2.stdout)
print(p3.stdout)
