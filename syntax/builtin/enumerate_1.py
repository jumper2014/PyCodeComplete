# coding=utf-8
# 循环访问序列中的元素和索引

sequence = [0, 1, 2, 3, 4, 5]
for index, item in enumerate(sequence):
    if index > 2:
        sequence[index] = item * item

print sequence