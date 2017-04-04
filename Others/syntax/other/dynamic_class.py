# coding=utf-8
# 根据参数动态生成类

def do_task(task_name):
    task = eval(task_name)()
    task.step1()



class Task1(object):
    def step1(self):
        print "task1"

class Task2(object):
    def step1(self):
        print "task2"

if __name__ == "__main__":
    do_task("Task1")
    do_task("Task2")


