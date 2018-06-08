# -*- coding:utf-8 -*-
import sys


def test1():
    try:
        i = 'y' + 1
    except Exception, e:
        print "===Exception===:", e
        print "===Exception===:", e.message
        print "===Exception===:", e.args
        pass
    print "yuan"

    pass


def test2():
    try:
        i = 'y' + 1
        print "yuan"
    except Exception, e:
        print e
    pass


def test3():
    try:
        i = 'y' + 1
        print "yuan"
    except:
        info = sys.exc_info()

        print info[0], ":", info[1]
    pass

    pass


def test4():
    try:
        try:
            raise ValueError('1')
        except TypeError:
            print 'Caught the type error'
    except ValueError:
        print 'Caught the value error!'


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
