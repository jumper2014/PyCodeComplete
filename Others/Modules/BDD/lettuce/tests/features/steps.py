#coding=utf-8
from lettuce import *

@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)
    print world.number

@step('I compute its factorial')
def compute_its_fatorial(step):
    world.number = factorial(world.number)
    print world.number

@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == expected, \
        "Got %d" % world.number

def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)