# coding=utf-8

import struct

# struct的pack函数把任意数据类型变成字符串
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
print struct.pack('>I', 10240099)

# unpack把str变成相应的数据类型
# 根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
