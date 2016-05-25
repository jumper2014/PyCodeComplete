# coding=utf-8
# 使用for else语句查找素数

for n in range(2, 10000):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        # loop through without finding
        print(n, "is a prime number")
