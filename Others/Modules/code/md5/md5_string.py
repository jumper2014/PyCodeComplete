# coding=utf-8

import md5

src = 'http://flv.srs.cloutropy.com/wasu/time1.flv'
m1 = md5.new()
m1.update(src)
md5_string = m1.hexdigest()
print(md5_string.upper())
