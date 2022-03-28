import requests as rs
par={"q":"pizza","oq":"pizza","ei":"T-sjX-v8GMOR4-EPgbuzqAs"}
r=rs.get("https://www.google.com/search?source=hp",params=par)
print(r.url)
f=open("yothoob.html","w+")
f.write(r.text)
print(r.url)