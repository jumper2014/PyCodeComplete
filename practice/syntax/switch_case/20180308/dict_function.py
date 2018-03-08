#!/usr/bin/env python
# coding=utf-8
# 用字典和函数代替switch case语法结构


def start_app():
    print("start app")


def stop_app():
    print("stop app")


def restart_app():
    print("restart app")


switch = {
    "start": start_app,
    "stop": stop_app,
    "restart": restart_app
}

if __name__ == '__main__':
    option = raw_input("input:")
    switch[option]()
