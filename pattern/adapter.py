"""
# @Time    : 2020/8/26 10:44
# @Author  : tmackan

适配器模式, 类似于接口转换器
用于集成统一不同的接口


"""
from typing import Callable, TypeVar

T = TypeVar("T")


class Dog(object):
    def __int__(self) -> None:
        self.name = "dog"

    def bark(self) -> str:
        return "woof!"


class Cat(object):
    def __init__(self) -> None:
        self.name = "Cat"

    def meow(self) -> str:
        return "meow!"


class Human:
    def __init__(self) -> None:
        self.name = "Human"

    def speak(self) -> str:
        return "hello"


class Adapter(object):
    def __init__(self, obj: T, **adapted_methods: Callable) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__


if __name__ == "__main__":
    objects = []
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    dog = Dog()
    objects.append(Adapter(dog, make_noise=dog.bark))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    for obj in objects:
        print(obj.make_noise())



























