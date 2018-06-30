### yagmail第三方库
- yagmail是一个为了尽可能简化发送邮件过程而开发的gmail/smtp客户端
- 一般3行代码就可以实现发送邮件功能了
- 如果你不介意代码行长度，1行也可以!
- 安装 pip install yagmail


### 例子
```
import yagmail

if __name__ == '__main__':
    yag = yagmail.SMTP(user="user1@163.com", password="user1password", host='smtp.163.com')

    contents = ['This is the body, and here is just text https://zhuanlan.zhihu.com/python2018',
                'You can find an file attached.', '/tmp/sample.png']

    yag.send(to='user2@hotmail.com',
             subject='yagmail sample',
             contents=contents)

```