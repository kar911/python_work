import threading
import time
from random import randint


class SharedCounter(object):

    def __init__(self, val=0):
        self.lock = threading.Lock()
        self.counter = val

    def increment(self):
        print("Waiting for a lock")
        self.lock.acquire()
        try:
            print('Acquired a lock, counter value: ', self.counter)
            self.counter = self.counter + 1
        finally:
            print('Released a lock, counter value: ', self.counter)
            self.lock.release()


def task(c):
    # picking up a random number
    r = randint(1, 5)
    # running increment for a random number of times
    for i in range(r):
        c.increment()
    print('Done')


if __name__ == '__main__':
    sCounter = SharedCounter()

    t1 = threading.Thread(target=task, args=(sCounter,))
    t1.start()

    t2 = threading.Thread(target=task, args=(sCounter,))
    t2.start()

    print('Waiting for worker threads')
    t1.join()
    t2.join()

    print('Counter:', sCounter.counter)

import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))

import time
def check(l,num):
    # import requests as rq
    # try:
    #     d = rq.get(l, verify=False,timeout=timeout)
    #     x=d.status_code
    #     return x
    # except rq.exceptions.SSLError:
    #     return 0
    # except rq.exceptions.ConnectionError:
    #     return 0
    if l != "6" and l!="4":
        time.sleep(2)
        return 1,num
    else:
        return 0,num


def option():
    import concurrent.futures as th
    d = [1,2,3,4]
    URLS=["1","2","3","4","5","6"]
    r=["a","b","c","d","e","f"]
    # with open("trialapp/nametorr.txt", "r") as t:
    #     for l in t.readlines():
    #         if l!="\n":
    #             d.append(l.split("/",3)[2])
    #             URLS.append(l)
    import concurrent.futures
    import urllib.request
    # URLS = ['http://www.foxnews.com/',
    #         'http://www.cnn.com/',
    #         'http://europe.wsj.com/',
    #         'http://www.bbc.co.uk/',
    #         'http://some-made-up-domain.com/']

    # Retrieve a single page and report the URL and contents
    def load_url(url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()
    # We can use a with statement to ensure threads are cleaned up promptly
    data=[]
    too=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url=[]#executor.submit(check,,10):[url,num] for url,num in URLS]
        s=list(zip(URLS,r))
        for i in s:
            future_to_url.append(executor.submit(check,i[0],i[1]))

        for future in concurrent.futures.as_completed(future_to_url):
            try:
                x=future.result()
                data.append(future.result()[0])
                too.append(future.result()[1])
            except Exception as exc:
                print("d",exc)
            else:
                print("dgg")
    print("goo")
    print(data)
    print(too)

option()