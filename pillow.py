from  PIL import Image
import os
for f in os.listdir('/home/kar/'):
    if f.endswith('.png'):
        print(f)
dog=Image.open('/home/kar/wall5.jpg')
dog.show()