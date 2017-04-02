说明：

1、get测试：http://steven-pc:8000/?test=data

2、通过curl来测试post数据：

curl -d "data=postdata" http://steven-pc:8000?test=post
data:postdata
test:post

3、支持中文：必须在头部加：#encoding=utf-8

三、CGIHTTPServer: 包含处理POST请求和执行CGIHTTPRequestHandler类。

参考 CGI介绍及使用Python来开发CGI应用示例