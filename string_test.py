# -*- coding:utf-8 -*-
def test1():
    str = 'ytx'
    str = list(str)
    str.remove('t')
    str = ''.join(str)
    print str
    pass


if __name__ == '__main__':
    test1()
