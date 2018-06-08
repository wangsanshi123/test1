# -*- coding:utf-8 -*-
import os


def test1():
    root = os.getcwd()
    file = 'temp.html'
    # abs = os.path.abspath()
    print "====root========", root
    # print "=====file=======", abs

    pass


def test2():
    root = os.getcwd()
    file = 'temp.html'
    path = os.path.join(root, file)
    print path
    pass


if __name__ == '__main__':
    # test1()
    test2()
