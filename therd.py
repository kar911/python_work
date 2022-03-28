import requests
from threading import Thread

# threding is for io bound tasks repatative/with different data
# multi processing is to cpu bound like crunching numbers etc

from queue import PriorityQueue
q = PriorityQueue(maxsize=5)
q.put(12)
q.put(130)
q.put(11)
q.put(14)
q.put(16)
print(q.queue)
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())
print(q.qsize())
print(b"b{\x00\x00\x00abc")

#
import concurrent.futures as th,time
import threading
# star=time.perf_counter()
def d0(second):
    time.sleep(1)
    if second > 2:
        print('in'+str(second))
        return 1# print("super cool")
    else:
        print('out' + str(second))
        return 0
# with concurrent.futures.ThreadPoolExecutor()as ex:
#     l=[]
#     for _ in range(10):
#         f=ex.submit(d0,1)
#         l.append(f)
#     for ll in concurrent.futures.as_completed(l):
#         print((ll.result()))

oo=map(abs,[1,2,3,4])
d=[1,2,3,4]
with th.ThreadPoolExecutor() as ta:
    tred = []
    df=[]
    for i in range(len(d)):
        tred1 = ta.submit(d0,next(oo))
        tred.append(tred1)
    for ll in th.as_completed(tred):
        if ll.result()== 0:
            df.append(0)
        else:
            df.append(1)

for i in range(len(d)-1):
    if df[i]==1:
        d.pop(i)

for i in d:
    print(i)
tt=[]
for _ in range(10):
    t=threading.Thread(target=d0,args=[2])
    t.start()
    tt.append(t)
for ttt in tt:
    ttt.join()
# t1=threading.Thread(target=d0)
# t2=threading.Thread(target=d0)
# t1.start()
# t2.start()
# t1.join()
# t2.join()


final=time.perf_counter()
print(round(final-star,3))
import requests
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')