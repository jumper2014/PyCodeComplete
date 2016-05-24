# coding=utf-8

# duplicate
some_list = ['a', 'b', 'c', 'm', 'n', 'c']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print duplicates

# intersection
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))

# difference
print(input_set.difference(valid))


