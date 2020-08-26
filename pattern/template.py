"""
# @Time    : 2020/8/26 14:13
# @Author  : tmackan


Define the skeleton of an algorithm in an operation, deferring some
steps to subclasses. Template Method lets subclasses redefine certain
steps of an algorithm without changing the algorithm's structure.

定义某个操作定义提供算法的骨架
模版方法让子类可以重新定义算法的步骤，而不需要改变算法的结构
基类只是声明算法的占位，派生的子类实现占位

"""


import abc


class AbstractClass(metaclass=abc.ABCMeta):
    """
    Define abstract primitive operations that concrete subclasses define
    to implement steps of an algorithm.
    Implement a template method defining the skeleton of an algorithm.
    The template method calls primitive operations as well as operations
    defined in AbstractClass or those of other objects.

    父类包含通用的实现
    子类可以新增特殊实现

    """

    def template_method(self):
        # 子类可以覆盖template_method内部方法的顺序
        # 这里只是抽象占位
        self._primitive_operation_1()
        self._primitive_operation_2()

    @abc.abstractmethod
    def _primitive_operation_1(self):
        pass

    @abc.abstractmethod
    def _primitive_operation_2(self):
        pass


class ConcreteClass(AbstractClass):
    """
    Implement the primitive operations to carry out
    subclass-specificsteps of the algorithm.
    子类实现特定的方法
    """

    def _primitive_operation_1(self):
        pass

    def _primitive_operation_2(self):
        pass


def main():
    concrete_class = ConcreteClass()
    concrete_class.template_method()


if __name__ == "__main__":
    main()
