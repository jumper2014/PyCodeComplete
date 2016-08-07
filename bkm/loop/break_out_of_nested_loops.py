# coding=utf-8
# 从多重循环中退出

for x in xrange(10):
    for y in xrange(10):
        for z in xrange(10):
            print x, y, z
            if x*y*z == 30:
                break
        else:
            continue
        break
    else:
        continue
    break

