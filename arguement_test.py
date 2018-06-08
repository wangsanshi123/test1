ints = [1, 2, 3, 1]
info = {'name': 'yuan', 'age': 13}


def test1(i, *b, **c):
    print i, '\n'
    if b:
        print b, '\n'
    if c:
        print c, '\n'


def test2(i, sql=None, **c):
    print i, '\n',
    if sql:
        print sql, '\n'
    # if b:
    #     print b, '\n'
    if c:
        print c, '\n'


pass

if __name__ == '__main__':
    # test1(1, 2, 3)
    # test1(1, 2, 3, m=2, n=3)
    # test1(1, *ints)
    # test1(1, **info)
    test2(1, sql='sql', **info)
