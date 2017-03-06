# coding=utf-8
# 嵌套类，内部类

# Quoted from http://www.geekinterview.com/question_details/64739:
#
# Advantages of inner class:
#
# Logical grouping of classes: If a class is useful to only one other class then it is logical to embed it in that class
# and keep the two together. Nesting such "helper classes" makes their package more streamlined.
# Increased encapsulation: Consider two top-level classes A and B where B needs access to members of A that would otherwise be declared private.
# By hiding class B within class A A's members can be declared private and B can access them. In addition B itself can be hidden from the outside world.
# More readable, maintainable code: Nesting small classes within top-level classes places the code closer to where it is used.
# The main advantage is organization. Anything that can be accomplished with inner classes can be accomplished without them.


class Car(object):          # 外部类
    class Door(object):     # 内部类
        def open(self):
            print('open door')

    class Wheel(object):
        def run(self):
            print('car run')

if __name__ == "__main__":
    car = Car()             # 实例化外部类
    backDoor = Car.Door()   # 实例化内部类 第一种方法

    frontDoor = car.Door()  # 因为car已经实例化外部类，再次实例化Car的内部类 第二种方法
    backDoor.open()
    frontDoor.open()
    wheel = car.Wheel()     # car已经实例化外部类，Wheel()再次实例化内部类
    wheel.run()             # 调用内部类的方法


