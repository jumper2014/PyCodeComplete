from urllib import urlopen

webpage = urlopen('http://www.cnblogs.com/IProgramming/')
txt = webpage.readline(45)
print txt
