# coding=utf-8

import qrcode
import sys
from PIL import Image

if __name__ == "__main__":
    url = sys.argv[1]
    print url
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image()
    img.show()
    # img.save("baidu.png")
