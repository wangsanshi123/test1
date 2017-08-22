# -*- coding:utf-8 -*-
import re


def testPattern1():
    '''匹配正负浮点数'''
    # result = re.search(r'-?\d+.\d+', 'faf-0.3')
    # result = re.search(r'-?\d+.\d+', 'faf0.03')
    result = re.search(r'^-?\d+.\d+$', '-1.23303')

    if result:
        print result.group()
    pass

def testPattern2():
    '''只能输入m-n位的数字'''

    result = re.search(r'^\d{3,5}', '12')
    result = re.search(r'^\d{3,5}', '123')
    result = re.search(r'^\d{3,5}', '1234')
    result = re.search(r'^\d{3,5}', '12345')
    result = re.search(r'^\d{3,5}$', '123456')

    if result:
        print result.group()
    pass


def testPattern3():
    '''匹配正整数'''
    result = re.search(r'^[1-9]\d*$', '3')
    result = re.search(r'^[1-9]\d*$', '35')
    result = re.search(r'^[1-9]\d*$', '356')

    if result:
        print result.group()
    pass


if __name__ == '__main__':
    # testPattern1()
    testPattern2()
    # testPattern3()
    pass
