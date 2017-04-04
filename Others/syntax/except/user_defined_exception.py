# coding=utf-8
# 用户自定义异常类

import math

class NegativeNumberError( ArithmeticError ):
   pass

def squareRoot( number ):
   if number < 0:
      raise NegativeNumberError, "Square root of negative number not permitted"
   return math.sqrt( number )

while 1:
   try:
      userValue = float( raw_input( "\nPlease enter a number: " ) )
      print squareRoot( userValue )
   # float raises ValueError if input is not numerical
   except ValueError:
      print "The entered value is not a number"
   # squareRoot raises NegativeNumberError if number is negative
   except NegativeNumberError, exception:
      print exception
   else:
      break