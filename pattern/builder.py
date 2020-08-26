"""
# @Time    : 2020/8/26 10:46
# @Author  : tmackan

建造者模式

Separate the construction of a complex object from its representation so
that the same construction process can create different representations.
分离复杂对象的构造和表示
同一构造过程，可以创建不同的表示
复杂的对象过程有不同的表示，一个操作往往很多种表示都会用到，将调用和组合移到上层中，便于解耦合


The "director" invokes "builder" services as it interprets the external format.
The "builder" creates part of the complex object each time it is called and maintains all intermediate state.
When the product is finished, the client retrieves the result from the "builder".
director调用builder服务
builder调用的时候，每次创建复杂对象的一部分，并且维护中间状态
当product结束后，client从builder得到结果


Affords finer control over the construction process.
Unlike creational patterns that construct products in one shot,
the Builder pattern constructs the product step by step under the control of the "director"

更好的控制构造的过程
不同于一键构造product
Builder模式在director的控制下, 一步接一步构造product

https://sourcemaking.com/design_patterns/builder

"""


import abc


class Director:
    """
    Construct an object using the Builder interface.
    """

    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder(metaclass=abc.ABCMeta):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    def __init__(self):
        self.product = Product()

    @abc.abstractmethod
    def _build_part_a(self):
        pass

    @abc.abstractmethod
    def _build_part_b(self):
        pass

    @abc.abstractmethod
    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


class Product:
    """
    Represent the complex object under construction.
    """

    pass


def main():
    concrete_builder = ConcreteBuilder()
    director = Director()
    director.construct(concrete_builder)
    product = concrete_builder.product


if __name__ == "__main__":
    main()