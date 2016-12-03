# coding=utf-8
# auth = shijian_app@163.com
# date = 2014-12-26

import urllib
from urllib2 import Request,urlopen,URLError
import httplib2,json

def YZZ_REQUEST(dest,method='POST',body={},headers={}):
    try:
        body_string = json.dumps(body)
        conn = httplib2.Http()
        response, content = conn.request(dest,method, body = body_string,headers = headers)
        return content
    except URLError,e:
        return e

def YZZ_REQUEST_HTTPS(dest,method='POST', body={},headers={}):
    try:
        body_string = json.dumps(body)
        request = Request(dest)
        for k in headers.keys():
            request.add_header(k, headers[k])
        request.add_data(body_string)
        request.get_method = lambda:method
        content = urlopen(request)
        return content.read()
    except URLError,e:
        print e

def test():
    uri_club = 'http://poff.cn:8899/club/sport/tennis/p/0'
    header={"AUTHORIZATION":"IPHONE"}
    body=dict(
        lon = '113.000',lat = '39.000',
        user_account = 'tnsi_anonymous',
        city = 'beijing')
    YZZ_REQUEST(uri_club, method='POST',body=body,headers=header)

    uri_rest = 'http://poff.cn:8881/testing/restful/'

    YZZ_REQUEST(uri_rest)
    YZZ_REQUEST(uri_rest,method='GET')
    YZZ_REQUEST(uri_rest,method='PUT')
    YZZ_REQUEST(uri_rest,method='POST')
    YZZ_REQUEST(uri_rest,method='DELETE')

    uri_wx_notice = 'http://182.92.160.37:8888/postto/onyn9tmItdL5GLeOaTSMJcpvhYkE/token/RYVWziFT2t9nUcJgHHJs7izdhXm6ejDPd88HiMa4hycqnaXTSVKk968Y848sCuf0WHyqEznDR9MWOKhK0aoZb2P9h5mE6cFCRSS-yjFy-Dg'
    YZZ_REQUEST(uri_wx_notice)

    YZZ_REQUEST_HTTPS(uri_rest)
    YZZ_REQUEST_HTTPS(uri_rest,method='PUT')
    YZZ_REQUEST_HTTPS(uri_rest,method='DELETE')

    YZZ_REQUEST_HTTPS(uri_club,body=body,headers=header)