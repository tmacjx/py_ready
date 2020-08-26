"""
# @Time    : 2020/8/26 14:12
# @Author  : tmackan

状态模式

Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.

容许一个对象当内部的状态改变时，更新它的行为
策略模式是一次绑定
状态模式是动态绑定

"""


import abc


class Context:
    """
    Define the interface of interest to clients.
    Maintain an instance of a ConcreteState subclass that defines the
    current state.

    """

    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()


class State(metaclass=abc.ABCMeta):
    """
    Define an interface for encapsulating the behavior associated with a
    particular state of the Context.
    """

    @abc.abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    """
    Implement a behavior associated with a state of the Context.
    """

    def handle(self):
        pass


class ConcreteStateB(State):
    """
    Implement a behavior associated with a state of the Context.
    """

    def handle(self):
        pass


def main():
    concrete_state_a = ConcreteStateA()
    context = Context(concrete_state_a)
    context.request()


if __name__ == "__main__":
    main()
