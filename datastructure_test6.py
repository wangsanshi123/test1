# -*- coding:utf-8 -*-
def test1():
    for i in range(10):
        print i
        i += 2
    for i in range(3):
        print "===i==",i
    pass
    print "===",i

if __name__ == '__main__':
    test1()
