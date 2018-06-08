# -*- coding:utf-8 -*-
import os


# 参考链接 http://blog.163.com/dengxiuhua126@126/blog/static/11860777201591103932498/
def test1():
    cmd = 'python1_2 cmd_test_temp.py'
    os.system(cmd)
    pass


def test2():
    r = os.popen('ping baidu.com')
    text = r.read()
    print text.decode('gbk')
    r.close()


if __name__ == '__main__':
    test1()
    # test2()
