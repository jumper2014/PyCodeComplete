#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

ignore_list = [


]

def get_text(section):
    with open("novel.txt", "a") as f:
        url = "http://www.jjwxc.net/onebook.php?novelid=3462043&chapterid={0}".format(section)
        response = requests.get(url)
        html = response.content.decode("gb2312", "ignore")

        # print(html)
        bs = BeautifulSoup(html, 'lxml')
        # print(bs.prettify())
        item = bs.select('.noveltext')[0]
        text = item.text.encode("utf-8")
        f.write(text)
        f.close()


if __name__ == "__main__":
    for section in range(1, 21):
        get_text(section)


