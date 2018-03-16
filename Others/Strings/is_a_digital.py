# coding=utf-8

text = "6665s78"
print text.isdigit()  # False, s


text = "6665.78"
print text.isdigit()  # False, .

text = "66658"
print text.isdigit()  # True
