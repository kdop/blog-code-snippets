class MyPackageParentException(Exception):
    pass


class CustomException1(MyPackageParentException):
    pass


class CustomException2(MyPackageParentException):
    pass


class MyClass(object):
    def do_stuff_1(self):
        raise CustomException1

    def do_stuff_2(self):
        raise CustomException2


m = MyClass()

try:
    m.do_stuff_1()
    ...
    m.do_stuff_2()
except CustomException1:
    ...  # handle CustomException1
except CustomException2:
    ...  # handle CustomException2
except MyPackageParentException:
    ...  # handle any other mypackage related problem
