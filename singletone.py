class Singleton(type):
    _all_instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._all_instances:
            print "create instance for ", cls
            cls._all_instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._all_instances[cls]


class X:
    __metaclass__ = Singleton

    def __init__(self, i):
        self.i = i


class Y:
    __metaclass__ = Singleton

    def __init__(self, i):
        self.i = i

x5 = X(5).i
x2 = X(2).i
assert x5 is x2

print Y(10).i
print Y(19).i

