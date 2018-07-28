### 二维码简介
- 二维码又称二维条码，常见的二维码为QR Code，QR全称Quick Response，是一个近几年来移动设备上超流行的一种编码方式，它比传统的Bar Code条形码能存更多的信息，也能表示更多的数据类型。
- 二维码中 有四种级别的纠错,这就是为什么二维码有残缺还能扫出来, 也就是为什么有人在二维码的中心位置加入图标。错误修正容量：L水平 7%的字码可被修正；M水平 15%的字码可被修正；Q水平 25%的字码可被修正；H水平 30%的字码可被修正

### 环境准备
- pip --default-timeout=500  install qrcode
- 防止安装时网络超时


### 例子
```
import qrcode

if __name__ == "__main__":
    url = "https://zhuanlan.zhihu.com/python2018"
    print(url)
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
```
别忘了，拿手机扫一扫看看效果

