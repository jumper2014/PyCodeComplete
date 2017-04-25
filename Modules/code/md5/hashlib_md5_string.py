# coding=utf-8
import hashlib
src = 'http://flv.srs.cloutropy.com/wasu/time1.flv'
m2 = hashlib.md5()
m2.update(src)
hashlib_md5_string = m2.hexdigest()
print(hashlib_md5_string.upper())
