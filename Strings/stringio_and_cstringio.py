# coding=utf-8
# 使用file API来存取内存中的文本内容

# 可以使用readline(), readlines(), seek()等方法来读取内存内容

# Find the best implementation available on this platform
try:
    from cStringIO import StringIO
except:
    from StringIO import StringIO

# Writing to a buffer
output = StringIO()
output.write('This goes into the buffer. ')
print >> output, 'And so does this.'

# Retrieve the value written
print output.getvalue()

output.close()  # discard buffer memory

# Initialize a read buffer
input = StringIO('Inital value for read buffer')

# Read from the buffer
print input.read()
