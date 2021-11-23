OBJECT_NUM = 200000

d = dict()
for i in range(0, OBJECT_NUM):
    d[str(i)] = type("MyClass", (object,), {"prop": 1})
