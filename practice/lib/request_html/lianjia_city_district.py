#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 获得链家网城区信息


from requests_html import HTMLSession

if __name__ == '__main__':
    session = HTMLSession()
    # 获取上海链家小区栏目页
    r = session.get('https://sh.lianjia.com/xiaoqu/')
    # 获得上海链家区县列表
    elements = r.html.xpath('/html/body/div[3]/div[1]/dl[2]/dd/div/div/a')
    # 区县英文和中文名列表
    en_names = list()
    ch_names = list()

    # element html代码 形如 <a href="/xiaoqu/pudong/" title="上海浦东小区二手房 ">浦东</a>
    for element in elements:
        for link in element.absolute_links:  # 遍历链接set
            en_names.append(link.split('/')[-2])
            ch_names.append(element.text)

    # 打印区县英文和中文名列表
    for index, name in enumerate(en_names):
        print(name, ch_names[index])

    """
        pudong 浦东
        minhang 闵行
        baoshan 宝山
        xuhui 徐汇
        putuo 普陀
        yangpu 杨浦
        changning 长宁
        songjiang 松江
        jiading 嘉定
        huangpu 黄浦
        jingan 静安
        zhabei 闸北
        hongkou 虹口
        qingpu 青浦
        fengxian 奉贤
        jinshan 金山
        chongming 崇明
        shanghaizhoubian 上海周边
    """
