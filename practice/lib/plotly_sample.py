#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import plotly.express as px
if __name__ == '__main__':
    iris = px.data.iris()
    fig = px.scatter(iris, x='sepal_width', y='sepal_length')
    fig.show()