# coding=utf-8
from HTMLParser import HTMLParser

page = '''''<sada>啊啊啊</sada><a href="http://click.union.360buy.com/JdClick /?unionId=75" class="f1"  style="padding-left:13px; padding-right:14px">京东商城</a></td><td><a href="http://www.letao.com /?source=hao123" class="f1">乐淘网上鞋城</a></td><td><a href="http://www.lashou.com/cl_today/w_3001" class="f2">拉手团购</a></td><td><a href="http://www.amazon.cn/?tag=2009hao123famousdaohang" class="f2">亚马逊</a></td><td><a href="http://www.vancl.com/?source=hao123mp"  class="f1">凡客诚品</a></td><td><a href="http://reg.jiayuan.com/st/?id=3237&url=/st /main.php" class="f1">世纪佳缘'''


class hp(HTMLParser):
    a_text = False

    def handle_starttag(self, tag, attr):
        if tag == 'a':
            self.a_text = True
            # print (dict(attr))

    def handle_endtag(self, tag):
        if tag == 'a':
            self.a_text = False

    def handle_data(self, data):
        if self.a_text:
            print (data)


yk = hp()
yk.feed(page)
yk.close()
