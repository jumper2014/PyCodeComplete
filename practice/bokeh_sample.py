#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


from bokeh.plotting import figure, output_file, show
# 创建图表
p = figure(plot_width=300, plot_height=300, tools="pan,reset,save")
# 图表中添加圆
p.circle([1, 2.5, 3, 2], [2, 3, 1, 1.5], radius=0.3, alpha=0.5)
# 定义输出形式
output_file("foo.html")
# 展示图表
show(p)

