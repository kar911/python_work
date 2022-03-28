import requests as rs
from io import BytesIO
from PIL import Image
r= rs.get("")
img =Image.open(BytesIO(r.content))
path="./IMAG."+img.format
try:
    img.save(path,img.format)
except IOError:
    print("not saved")