# -*- coding:utf-8 -*-
import json
import re
from time import strftime, localtime

import datetime
import requests


def test1():
    result = "ytx".encode("utf-8")
    print result

    pass


def test2():
    # result = "袁泰星".encode("utf-8")
    result = u'中文测试'.encode('utf-8')
    result = '\xe4\xb8\xad\xe6\x96\x87\xe6\xb5\x8b\xe8\xaf\x95'.decode('utf-8')
    result = '\xe4\xb8\xad\xe6\x96\x87\xe6\xb5\x8b\xe8\xaf\x95'.decode('unicode-escape')
    result = '\xe4\xb8\xad\xe6\x96\x87\xe6\xb5\x8b\xe8\xaf\x95'.decode('string-escape')
    print result

    pass


def test3():
    result1 = u'中文测试'.encode('utf-8')
    result2 = u'中文测试'.encode('unicode-escape')
    result3 = '中文测试'.encode('string-escape')
    result4 = '\xe4\xb8\xad\xe6\x96\x87\xe6\xb5\x8b\xe8\xaf\x95'.decode('utf-8')
    result5 = '\xe4\xb8\xad\xe6\x96\x87\xe6\xb5\x8b\xe8\xaf\x95'.decode('unicode-escape')
    result6 = '\xe4\xb8\xad\xe6\x96\x87\xe6\xb5\x8b\xe8\xaf\x95'.decode('string-escape')
    result7 = '\xE8\xBF\x99\xE4\xB8\xAA'.decode('string-escape')
    # print result1
    # print result2
    print "result3",result3
    print "result4",result4
    print "result5",result5
    print "result6",result6
    print "result7",result7

    pass


def test4():
    ''' 'u'代表的是Unicode类型，要用Unicode-escape或者utf-8解码,'x'代表的是string类型，要用string-escape解码'''
    result1 = u'中文测试'.encode('utf-8')
    result2 = u'中文测试'.encode('unicode-escape')
    result3 = '中文测试'.encode('string-escape')
    result4 = '\u4e2d\u6587\u6d4b\u8bd5'.decode('utf-8')
    result5 = '\u4e2d\u6587\u6d4b\u8bd5'.decode('unicode-escape')
    result6 = '\u4e2d\u6587\u6d4b\u8bd5'.decode('string-escape')
    result_temp = u'\u8fd9\u4e2a'.encode('unicode-escape').decode('unicode-escape')



    print "result1:", result1
    print "result2:", result2
    print "result3:", result3
    print "result4:", result4
    print "result5:", result5
    print "result6:", result6
    print "result_temp:", result_temp

    pass


def test5():
    s = u'\xe4\xb8\xad\xe6\x96\x87\xe6\xb5\x8b\xe8\xaf\x95'
    a = s.encode('unicode_escape').decode('string_escape')
    print a


def test6():
    s = u"中文测试"
    s_utf = s.encode('utf-8')
    s_gbk = s.encode('gbk')

    print "s_utf:", s_utf
    print "s_gbk", s_gbk


def test7():
    # with open("ips.json", "r") as f:
    #     result = f.read()
    #     # result = re.sub(r"(u)\s*?'", "", str(result))
    result = ""
    result = re.sub(r"(u)\s*?'", "", str(result))
    with open("ips3.json", 'w') as f2:
        f2.write(result)
    print result


pass


def getIpFromJson():
    with open("ips.json", "r") as f:
        results = json.load(f)[u"result"]
        print results
        with open("ips2.json", "w") as f2:
            f2.write(json.dumps(results))


def getIpFromMipu():
    with open("ips.json", "w") as f:
        result = requests.get(
            "http://proxy.mimvp.com/api/fetch.php?orderid=860170907095435229&num=500&country_group=3&http_type=1&result_fields=1,2,8&result_format=json").text
        result = json.loads(result)
        date = strftime("%Y-%m-%d %H:%M", localtime())

        result["date"] = date
        result = json.dumps(result)
        f.write(str(result))


def getIp(savedTime=1):
    '''根据时间判断,savedTime 存活时间（分钟）'''
    # with open("ips.json", "w") as f:
    #     f.read()
    date = json.load(open("ips.json", "r"))["date"]

    now = datetime.datetime.now()

    delta = datetime.timedelta(minutes=savedTime)
    now = now - delta
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    if now > date:
        print "存活期已过,需要更新ip"
        getIpFromMipu()
        print "更新ip完毕"
    else:
        print "最新ip"
    pass


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
    # test5()
    # test6()
    # test7()
    # getIpFromMipu()
    # getIpFromJson()
    # getIp()
