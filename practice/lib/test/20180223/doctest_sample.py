#!/usr/bin/env python
# coding=utf-8


def add(x, y):
    """ add two number or string
    >>> add(1, 2)
    3

    >>> add("hello", " world")
    'hello world'

    >>> add(1, 2.0)
    3

    >>> add("hello", " python")  # doctest: +ELLIPSIS
    'hello ...'

    """
    return x+y


if __name__ == '__main__':
    import doctest
    doctest.testmod()