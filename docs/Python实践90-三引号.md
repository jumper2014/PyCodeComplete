### 三引号的作用
- 表示多行字符串，所见即所得
- 用于定义docstring（文档注释）

### 多行字符串
```
errHTML = """<HTML><HEAD><TITLE>Friends CGI Demo</TITLE></HEAD><BODY><H3>ERROR</H3><B>%s</B><P><FORM><INPUT TYPE=button VALUE=BackONCLICK="window.history.back()"></FORM></BODY></HTML>"""
cursor.execute("""CREATE TABLE users (login VARCHAR(8), uid INTEGER,prid INTEGER)""")
```
- 注意：行尾换行符会被自动包含到字符串中，但是可以在行尾加上 \ 来避免这个行为。下面的示例： 可以使用反斜杠为行结尾的连续字符串，它表示下一行在逻辑上是本行的后续内容:
```
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
- 将生成以下输出（注意，没有开始的第一行）:
```
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

### docstring
- 文档字符串的标准格式
文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。 强烈建议 你在你的函数中使用文档字符串时遵循这个惯例。
```
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""
```
- PEP 257 建议即使是一行的docstring也应该使用三引号，因为这样便于以后的扩展。