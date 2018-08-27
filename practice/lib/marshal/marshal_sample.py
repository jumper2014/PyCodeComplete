#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import marshal

if __name__ == '__main__':
    data1 = ['author', 100, True]
    data2 = {"name": 'Python', "Age": 30}

    # 把这些数据序列化到文件中，注：文件必须以二进制模式打开
    output_file = open("marshal.out", 'wb')
    marshal.dump(data1, output_file)
    marshal.dump(data2, output_file)
    output_file.close()

    # 从文件中读取序列化的数据
    input_file = open('marshal.out', 'rb')
    data1 = marshal.load(input_file)
    data2 = marshal.load(input_file)
    print(data1)
    print(data2)

    out_string = marshal.dumps(data1)  # marshal.dumps()返回是一个字节串，该字节串用于写入文件
    open('out.bin', 'wb').write(out_string)

    file_data = open('out.bin', 'rb').read()
    real_data = marshal.loads(file_data)
    print(real_data)