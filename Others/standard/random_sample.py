# coding=utf-8
# 随机函数

import random
# 0-1
print random.random()

# 随机浮点数
print random.uniform(1, 10)

# randint
print random.randint(10, 20)


print random.randrange(10, 100, 2)


print random.choice("learn python")
print random.choice(['hello', 'world', 'yes'])
print random.choice(('hello', 'world', 'yes'))

print random.choice('abcdefg!@#$%^&*')

lst = range(100)
random.shuffle(lst)
print lst

lst = range(100)
print random.sample(lst, 5)