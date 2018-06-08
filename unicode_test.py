# -*- coding:utf-8 -*-
def test1():
    # print u'袁'+'泰' #错误写法
    print u'袁' + u'泰'  # 正确
    print '袁' + '泰'  # 正确

    pass


def test2():
    with open('temp.txt', 'r') as f:
        result = f.read().decode('utf-8')
        # result = f.read() #错误写法
        print u'开头' + result


if __name__ == '__main__':
    # test1()
    test2()
