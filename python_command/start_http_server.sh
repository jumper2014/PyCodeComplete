#!/usr/bin/env bash
# start a simple http server with port
# then you can curl or wget file with http://ip:9999

python -m SimpleHTTPServer 9999

# for python 3
# python3 -m http.server