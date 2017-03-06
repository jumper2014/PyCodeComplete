# coding=utf-8


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Student object (name %s)" % self.name

    __repr__ = __str__

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer')
        if value < 0 or value > 100:
            raise ValueError('score must between on ~ 100!')

        self._score = value

if __name__ == "__main__":
    s = Student("Mike")
    s.score = 60
    print s.score

    print Student("Wiki")
    print repr(Student("hello"))