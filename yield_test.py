def test():
    for i in range(5):
        print i
        yield i


def test1():
    test()

    pass


def test2():
    next(test())


if __name__ == '__main__':
    # test1()
    test2()
