# coding=utf-8
# range和xrange

# xrange 和 range 这两个基本上都是在循环的时候用
for i in range(0, 100):
    print i

for i in xrange(0, 100):
    print i

# range会直接生成一个list对象
# 而xrange则不会直接生成一个list，而是每次调用返回其中的一个值：
# xrange 用法与 range 完全相同，所不同的是生成的不是一个list对象，而是一个生成器。
# 要生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间。

a = xrange(0,100)
print type(a)
print a
print a[0], a[99]