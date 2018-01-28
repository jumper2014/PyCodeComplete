#!/usr/bin/env python
# coding=utf-8

# False
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# True
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# True
print '\'xxx\' is str?', isinstance('xxx', str)
# True
print 'b\'xxx\' is str?', isinstance(b'xxx', str)