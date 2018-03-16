# coding=utf-8
import urllib2
import cookielib

# declare cookiejar object to save cookie
cookie = cookielib.CookieJar()
# use urllib2's HTTPCookieProcess object to create cookie handler
handler = urllib2.HTTPCookieProcessor(cookie)
#create opener via handler
opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value