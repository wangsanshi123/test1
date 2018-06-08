# -*- coding:utf-8 -*-
import os
from time import strftime, localtime


def test1(msg):
    '''追加模式，若果没有就创建'''
    now = strftime("%Y-%m-%d-%H", localtime())
    file = now + ".txt"
    with open(file, "a") as f:
        f.write(msg)

    pass


def test2():
    "读取指定的行数"
    with open("D:\\gsmarena-data\\RedmiNote3.csv", "r") as f:
        # print f.read()

        # print f.readline() #读取首行
        # print f.readline(10) #读取指定字符数
        # print type(f.readlines())
        print f.readlines()[0]

    pass


if __name__ == '__main__':
    # test1("ytx")
    test2()
