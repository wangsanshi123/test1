# -*- coding:utf-8 -*-
import chardet
import requests
from bs4 import BeautifulSoup


def visitiInternet(i):
    # ips = ["180.112.219.199", '111.199.12.87', '121.56.37.12']
    # ips = ["113.121.168.197",]
    # proxies = {"http": ips, }
    proxies = {"http": "171.39.114.152:8123", 'http': '27.212.152.9:8080'}
    r = requests.get('http://tool.chinaz.com/ipwhois', proxies=proxies)
    r.encoding = chardet.detect(r.content)['encoding']
    print r.text
    # if r is None:
    #     print "无法爬取，可能ip被封"
    # else:
    #     soup = BeautifulSoup(r.text, 'lxml')
    #     soup.prettify()
    #     divs = soup.find_all('div', id='lg')
    #     if len(divs):
    #         print "正在爬取....",str(i)


pass

for i in range(1):
    visitiInternet(i)
