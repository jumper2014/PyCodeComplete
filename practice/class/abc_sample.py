#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from abc import ABCMeta, abstractmethod


class People(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_name(self):
        pass


class Student(People):
    def show_name(self):
        print('Student: {0}'.format(self.name))


class Teacher(People):
    def show_name(self):
        print('Teacher: {0}'.format(self.name))


if __name__ == '__main__':
    # TypeError: Can't instantiate abstract class People with abstract methods show_name
    # p = People("Python")

    student = Student("Li")
    student.show_name()

    teacher = Teacher("Wang")
    teacher.show_name()