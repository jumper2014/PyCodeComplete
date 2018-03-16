# coding=utf-8

from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for (variable, value) in attrs:
                    if variable == "href":
                        self.links.append(value)


if __name__ == "__main__":
    html_code = """ <a href="www.google.com"> google.com</a> <A Href="www.pythonclub.org"> PythonClub </a> <A HREF = "www.sina.com.cn"> Sina </a> """
    hp = MyHTMLParser()
    hp.feed(html_code)
    hp.close()
    print(hp.links)
