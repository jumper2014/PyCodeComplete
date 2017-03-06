# coding=utf-8
"""
下载文件并保存
"""

import requests

def download_file(url, filename):
    # local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:   # filter out keep-alive new chunks
                fd.write(chunk)