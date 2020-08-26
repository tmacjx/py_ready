"""
# @Time    : 2020/8/25 16:06
# @Author  : tmackan

代理模式

Provide a surrogate or placeholder for another object to control access
to it or add other responsibilities.

提供替代或者占位, 控制对象的访问或者增加新的功能


    RealSubject和Proxy的接口名称应该一致
    客户端可以使用RealSubject或者Proxy而不需要改动代码
    该抽象类不一定需要，重点是RealSubject或者Proxy的使用无差别

"""

import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Proxy(Subject):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # ...
        self._real_subject.request()
        # ...


class RealSubject(Subject):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        pass


def main():
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()


if __name__ == "__main__":
    main()