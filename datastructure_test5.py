# -*- coding:utf-8 -*-
'''所以，对于不变对象来说，调用对象自身的任意方法，
也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，
这样，就保证了不可变对象本身永远是不可变的。'''


def list_test():
    a = ['y', 't', 'x']
    a_temp = a.sort()
    print(a)
    print(a_temp)


def str_test():
    b = 'ytx'
    b_temp = b.replace('y', "Y")
    print(b)
    print(b_temp)


if __name__ == '__main__':
    list_test()
    str_test()
