# coding=utf-8
# 列表推导，字典推导，集合推导

# list comprehension
a = [1, 2, 3, 4, 5, 6]
even_squares = [x**2 for x in a if x % 2 == 0]
print even_squares

# dict comprehension
student_ranks = {"fang": 88, "liu": 77, "tian": 99}
rank_dict = {rank: name for name, rank in student_ranks.items()}
print rank_dict

# set comprehension
name_len_set = {len(name) for name in student_ranks.keys()}
print name_len_set
