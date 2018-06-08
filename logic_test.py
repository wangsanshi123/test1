def test1():
    if 'false' is not 'false' and 'False':
        print 'not'
    else:
        print 'is'
    pass


def test2():
    if 'false' is not 'false' or 'False':
        print 'not'
    else:
        print 'is'
    pass


if __name__ == '__main__':
    test1()
    test2()
