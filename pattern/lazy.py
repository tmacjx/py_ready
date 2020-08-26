"""
# @Time    : 2020/8/25 16:07
# @Author  : tmackan

懒加载

"""


class lazy_property(object):
    """
    利用描述符, 来hock属性访问
    """
    def __init__(self, func):
        self.func = func
        self.name = self.func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        val = self.func(instance)
        instance.__dict__[self.name] = val
        return val


class A(object):

    @lazy_property
    def run(self):
        print("run")
        return "ok"


a = A()
print(a.run)
print(a.run)




