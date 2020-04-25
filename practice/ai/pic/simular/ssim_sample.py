#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian


# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/17 14:26
# @Author  : xhh
# @Desc    : 结构相似度量，计算图片之间的相似度
# @File    : difference_image_ssim.py
# @Software: PyCharm
from skimage.measure import compare_ssim
from scipy.misc import imread
import numpy as np

# 读取图片
img1 = imread('../dataset/100002.png')
img2 = imread('../dataset/100001.png')
img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
print(img1.shape)
print(img2.shape)
ssim = compare_ssim(img1, img2, multichannel=True)
print(ssim)
