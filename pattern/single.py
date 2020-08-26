"""
# @Time    : 2020/8/25 16:06
# @Author  : tmackan

单例模式

"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, '_instance'):
            return cls._instance
        cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        # cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super(Singleton, self).__init__()


s = Singleton()
s2 = Singleton()
print(id(s) == id(s2))


class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        print("call type enter")
        if hasattr(cls, "_instance"):
            return cls._instance
        cls._instance = super(SingletonType, cls).__call__(cls, *args, **kwargs)
        print("call ", cls)
        return cls._instance


class Foo(metaclass=SingletonType):
    def __new__(cls, *args, **kwargs):
        print("new enter")
        print("new ", cls)


foo = Foo()
foo1 = Foo()
print(foo == foo1)


def single_wrapper(cls):
    instance = []

    def wrapper(*args, **kwargs):
        if not instance:
            instance.append(cls(*args, **kwargs))
        return instance[0]
    return wrapper


@single_wrapper
class Foo(object):
    pass


foo = Foo()
foo1 = Foo()
print(foo == foo1)






