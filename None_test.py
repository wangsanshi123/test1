# -*- coding:utf-8 -*-
def test1():
    str = ""
    if str:
        print "str is:", str
    else:
        print "str type is", type(str)
    if str is None:
        print "str is none"

    if str == 'None':
        print " str == None"

    if str == "":
        print " str is null"

    pass
def test2():
    str = None
    if str:
        print "str is:", str
    else:
        print "str type is", type(str)
    if str is None:
        print "str is none"

    if str == 'None':
        print " str == None"

    if str == "":
        print " str is null"
    pass

if __name__ == '__main__':
    # test1()
    test2()
