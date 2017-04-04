# coding=utf-8
'''
# prerequisite:
#   based on Python 2.x
#   need Python XXX module
#   make XXXXX command is in PATH

# usage:
    1) change the variables:XXX,XXX
    2) thisscript.py arg1 arg2 arg3
    
# process:
    1) step1
    2) step2
    3) step3
    4) step4
    5) step5
  
# know issues:
    1) issue1
    2) issue2
# Other
    Any issues or improvements please contact xxx@126.com
'''



import sys

def loop():
    pass

if __name__ == '__main__':
    print len(sys.argv)
    for i in sys.argv:
        print i

    if not len(sys.argv) == 4:
        print __doc__
    else:
        loop()
