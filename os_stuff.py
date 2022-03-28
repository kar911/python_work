for dirpath,dirnames,filenames in os.walk("/home/kar/trials_for_code"):
    print("crrpath: ",dirpath)
    print("dirr: ",dirnames)
    print("fname: ",filenames)
    print()
os.makedirs("1sdsad1")
os.rmdir("sdsad")
os.rename("sdsad","coolcool")
print(os.listdir())
print(os.stat("text").st_size)
oo=os.stat("text").st_mtime
print(dtm.datetime.fromtimestamp(oo))
os.path.join("/home/kar/trials_for_code","dasdsad.txt")
os.system("/home/kar/trials_for_code/text")
import os ,time

# import datetime as dtm

os.chdir("/home/kar/trials_for_code")
import sys
print(sys.platform)
print("dsadsa")

src = '/usr/bin/python'
dst = '/tmp/python'

os.symlink(src, dst)
path = os.readlink( dst )
print(path)

# for l version we pass the ' ' and then put argumrnt in the function
#     but in v version we first create a list an then pass that list to the function as argument like below
#     we  choose 'l' variable and put it to the v typr version of spawn and exec functions
l=[" "]

os.spawnl(os.P_WAIT,"/home/kar/Desktop/shot/TtoS.sh",' ')
os.spawnle(os.P_WAIT,"/home/kar/Desktop/shot/TtoS.sh",' ',os.environ)
os.spawnlp(os.P_WAIT,"/home/kar/Desktop/shot/TtoS.sh",' ')
os.spawnlpe(os.P_WAIT,"/home/kar/Desktop/shot/TtoS.sh",' ',os.environ)
os.spawnv(os.P_NOWAIT,"/home/kar/Desktop/shot/TtoS.sh",l)
os.spawnve(os.P_NOWAITO,"/home/kar/Desktop/shot/TtoS.sh",l,os.environ)
os.spawnvp(os.P_WAIT,"/home/kar/Desktop/shot/TtoS.sh",l)
os.spawnvpe(os.P_WAIT,"/home/kar/Desktop/shot/TtoS.sh",l,os.environ)

os.execvpe("/home/kar/Desktop/shot/TtoS.sh",l,os.environ)
os.execvp("/home/kar/Desktop/shot/TtoS.sh",l)
os.execve("/home/kar/Desktop/shot/TtoS.sh",l,os.environ)
os.execv("/home/kar/Desktop/shot/TtoS.sh",l)
os.execlpe("/home/kar/Desktop/shot/TtoS.sh"," ",os.environ)
os.execl("/home/kar/Desktop/shot/TtoS.sh"," ")
os.execle("/home/kar/Desktop/shot/TtoS.sh"," ",os.environ)
os.execlp("/home/kar/Desktop/shot/TtoS.sh"," ")
print(os.ctermid()+"dasd")
print(os.getuid())
print(os.getresuid())
print(os.supports_fd)
os.system("""
cd ..
cd ..
ls -la |grep py
            """)
dd=os.popen("""
ls -la |grep py
            """,'r',2)
print(dd.read())
pi=os.fork()
if not pi:
    for step in range(3):
        print(f"{os.getpid()} child {step}\n")
        pif=os.fork()
        if not pif:
            for step in range(3):
                print(f"{os.getpid()} child pif {step}\n")
                time.sleep(1)
        else:
            for step in range(3):
                os.waitpid(pif,os.WNOHANG)
                print(f"{os.getpid()} parent pif {step}\n")
                time.sleep(1)
        time.sleep(1)

else:
    for step in range(3):
        print(f"{os.getpid()} parent {step}\n")
        print()
        time.sleep(1)

# 4883 parent 0
#
#
# 4890 child 0
#
# 4890 parent pif 0
#
# 4891 child pif 0
#
# 4883 parent 1
#
#
# 4890 parent pif 1
#
# 4891 child pif 1
#
# 4883 parent 2
#
#
# 4890 parent pif 2
#
# 4891 child pif 2


# 4928 parent 0
#
#
# 4935 child 0
#
# 4935 parent pif 0
#
# 4936 child pif 0
#
# 4928 parent 1
#
#
# 4935 parent pif 1
#
# 4936 child pif 1
#
# 4928 parent 2
#
#
# 4935 parent pif 2
#
# 4936 child pif 2
