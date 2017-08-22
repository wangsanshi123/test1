# -*- coding:utf-8 -*-

def fun1():
    proxies = {"http": "171.39.114.152:8123", 'http': '27.212.152.9:8080','http':'121.225.85.104:8118'}
    print proxies.get("http")
    pass



if __name__ == '__main__':
    fun1()