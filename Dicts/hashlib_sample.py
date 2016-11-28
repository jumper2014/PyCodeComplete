# coding=utf-8
# hashlib 涉及安全散列和消息摘要，提供多个不同的加密算法接口，如SHA1、SHA224、SHA256、SHA384、SHA512、MD5等
import hashlib

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()


# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()


# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

m = hashlib.md5()   # 创建hash对象，md5:(message-Digest Algorithm 5)消息摘要算法,得出一个128位的密文
print m             # <md5 HASH object @ 000000000254ADF0>
m.update('BeginMan') # 更新哈希对象以字符串参数
print m.digest()    # 返回摘要，作为二进制数据字符串值
print m.hexdigest() # 返回十六进制数字字符串    0b28251e684dfbd9102f8b6f0281c0c5
print m.digest_size # 16
print m.block_size  # 64

# new()创建指定加密模式的hash对象
h = hashlib.new('md5')
print h     # <md5 HASH object @ 000000000260BDB0>
h2 = hashlib.new('ripemd160','what')
print h2    # <ripemd160 HASH object @ 000000000271B9F0>
h.update('beginman')
print h.hexdigest() # 666fc5baa93a7fb207c5bfff03b67732
# 等效
s = hashlib.md5()
s.update('beginman')
print s.hexdigest() # 666fc5baa93a7fb207c5bfff03b67732

print h2.hexdigest()    # 9c1185a5c5e9fc54612808977ee8f548b2258d31



