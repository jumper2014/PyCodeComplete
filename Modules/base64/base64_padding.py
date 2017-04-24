# coding=utf-8

# base64模块包含一些函数，将二进制数据转换为适合使用纯文本协议传输的ASCII子集

import base64

# load this source file and strip the header
with open(__file__, 'rt') as inputs:
    raw = inputs.read()
    initial_data = raw.split('#end_pymotw_header')[1]

encoded_data = base64.b64encode(initial_data)
num_initial = len(initial_data)

# there will never be more than 2 padding bytes
padding = 3 - (num_initial % 3)

print '%d bytes before encoding' %num_initial
print 'expect %d padding bytes' %padding
print '%d bytes after encoding' %len(encoded_data)
print
print encoded_data
