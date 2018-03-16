# coding=utf-8

import json

data = [{'a': 'A',
         'b': (2, 4),
         'c': 3.0
         }]
print 'Data:', repr(data)

data_string = json.dumps(data)
print 'Json:', data_string

decoded = json.loads(data_string)
print "Decoded:", decoded
