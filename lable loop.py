import random
lists = [[random.randint(0, 100) for i in range(10)] for i in range(10)]

class Label(object):
    class __break(Exception):
        def __init__(self, ctx):
            self.ctx = ctx

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return isinstance(exc_val, self.__break) and exc_val.ctx is self

    def break_(self):
        raise self.__break(self)

found = False
with Label() as search:
 for li in lists:
     for val in li:
         if val == 42:
             found = True
             search.break_()
         print(val)