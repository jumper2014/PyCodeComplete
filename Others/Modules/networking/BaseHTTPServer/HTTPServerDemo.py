# encoding=utf-8

"""
Created on 2012-11-7

@author: Steven
http://www.lifeba.org
基于BaseHTTPServer的http server实现，包括get，post方法，get参数接收，post参数接收。
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import io
import shutil
import urllib


class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.process(2)

    def do_POST(self):
        self.process(1)
        
    def process(self,type):
        
        content = ""
        if type == 1: # post方法，接收post参数
            datas = self.rfile.read(int(self.headers['content-length']))
            datas = urllib.unquote(datas).decode("utf-8", 'ignore')  # 指定编码方式
            datas = trans_dicts(datas)   # 将参数转换为字典
            if datas.has_key('data'):
                content = "data:"+datas['data']+"\r\n"
                
        if '?' in self.path:
            query = urllib.splitquery(self.path)
            action = query[0] 
                     
            if query[1]:    # 接收get参数
                query_params = {}
                for qp in query[1].split('&'):
                    kv = qp.split('=')
                    query_params[kv[0]] = urllib.unquote(kv[1]).decode("utf-8", 'ignore')
                    content += kv[0]+':'+query_params[kv[0]]+"\r\n"
                    
            # 指定返回编码
            enc = "UTF-8"
            content = content.encode(enc)          
            f = io.BytesIO()  
            f.write(content)  
            f.seek(0)  
            self.send_response(200)  
            self.send_header("Content-type", "text/html; charset=%s" % enc)  
            self.send_header("Content-Length", str(len(content)))  
            self.end_headers()  
            shutil.copyfileobj(f, self.wfile)


def trans_dicts(params):
    dicts = {}
    if len(params) == 0:
        return
    params = params.split('&')
    for param in params:
        dicts[param.split('=')[0]] = param.split('=')[1]
    return dicts
       
if __name__ == '__main__':
    
    try:
        server = HTTPServer(('', 8000), MyRequestHandler)
        print 'started httpserver...'
        server.serve_forever()

    except KeyboardInterrupt:
        server.socket.close()
    
    pass
