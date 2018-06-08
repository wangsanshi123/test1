# -*- coding:utf-8 -*-
import chardet
import requests


def fun1(url):
    r = requests.get(url)
    r.encoding = chardet.detect(r.content)['encoding']
    print r.text


def test1(url):
    "useragent"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"

    headers = {"User-Agent": user_agent}
    requests.get(url, headers=headers)
    pass


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    # fun1(url)
    test1(url)
