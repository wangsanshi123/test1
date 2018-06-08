# -*- coding:utf-8 -*-

# "详见https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000"

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def test1(*args):
    return lazy_sum(*args)


def test2():
    return count()


def divide2(x):
    return x / 2


def divide3(x):
    return x / 3


def test3(x):
    try:
        temp = divide3(x)
    except:
        temp = 0
        pass

    result = divide2(temp)
    return result


if __name__ == '__main__':
    # result = test1(1, 2)
    # print result
    # result = result()
    # print result
    # print test2()
    # print test2()[0]()
    # print test2()[1]()
    # print test2()[2]()
    print test3('y')
