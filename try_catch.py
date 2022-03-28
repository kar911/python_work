s=(1,2,3,5,6)
try:
    print(s[1])
except(Exception):
    print("sorry for inconvenience")
else:
    print('great')
class d:
    def find(self):
        c = {'21': 211, '23': 23}
        g="kartik moyade".split(" ",2)
        print(g[0])
        print(c.get("231","sorry not found"),c["21"])
f=d()
f.find()
import subprocess
v=subprocess.run("ls | grep '.py'".split(),capture_output=True,text=True)
print(v)
