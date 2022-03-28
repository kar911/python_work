import simplejson as js 
import os
if os.path.isfile('./ages.json') and os.stat('./ages.json').st_size !=0:
    file =open("./ages.json","r+")
    data =js.loads(file.read())
    print("current height in inch is"," adding a inch")
    data =not data
    print("new height is ")
else:
    file=open("./ages.json","w+")
    data=True
    print("default",data)

file.seek(0)
file.write(js.dumps(data))
import pandas