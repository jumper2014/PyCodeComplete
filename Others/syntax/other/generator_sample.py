# coding=utf-8


def create_generator():
    mylist = range(10)
    for i in mylist:
        yield i*i

my_generator = create_generator()
print my_generator
for i in my_generator:
    print i
