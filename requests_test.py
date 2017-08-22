# -*- coding:utf-8 -*-
import chardet
import requests


def fun1(url):
    r = requests.get(url)
    r.encoding = chardet.detect(r.content)['encoding']
    print r.text


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    fun1(url)
