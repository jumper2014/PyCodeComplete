#!/user/bin/env python
# -*-coding:utf-8-*-
# @time       : 16/11/8 12:09
# @Author     : Zhangxy
# @File       : 001baiduSearch.py
# @Software   : PyCharm

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.find_element_by_link_text(u"登录").click()
# driver.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
# driver.find_element_by_link_text('搜索设置').click()


