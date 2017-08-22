# -*- coding:utf-8 -*-
import ssl
import urllib2


def fun1(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html


def fun2(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    context = ssl._create_unverified_context()
    response = None
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request, context=context)
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    print response.read()


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    fun1(url)
    # fun2(url)