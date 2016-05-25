# coding=utf-8
# 类中的列表成员变量是所有对象共享的，因为列表是引用

class Student(object):
    age = 0
    friends = []

    def meet_new_friend(self, name):
        self.friends.append(name)

if __name__ == "__main__":
    a = Student()
    a.age = 10
    a.meet_new_friend("friend1")
    b = Student()
    b.age = 12
    b.meet_new_friend("friend2")

    print b.friends  # ['friend1', 'friend2']

