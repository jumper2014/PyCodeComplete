#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import pytesseract
from PIL import Image

if __name__ == '__main__':
    print(pytesseract.image_to_string(Image.open('zen.png')))