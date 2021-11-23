OBJECT_NUM = 200000


class MyClass(object):
    prop = 1


d = dict()
for i in range(0, OBJECT_NUM):
    d[str(i)] = MyClass()
