import re


def test1():
    string = "orum.php?mod=forumdisplay&fid=1220&page=2"
    print re.search(r'.*?&page=(\d*$)', string).groups()[0]


def test2():
    # str1 = "3 hrs 24 mins ago"
    str1 = "17 days ago"
    result = re.search(r"(.*)hrs(.*)mins", str1)
    if result:
        print result.groups()[0].strip()
        print result.groups()[1].strip()
    else:
        result = re.search(r"(.*)days", str1)
        if result:
            print result.groups()[0]


def test3():
    s = 'Ihave a dogs, you have a dog, he have a dogs'
    s = re.sub(r'(dog)s', 'cat', s)
    print s


def test4():
    available = "Available. Released 2016, October"
    available = "Available. eleased 2016, October"
    result = re.sub(r'(.*?[rR]eleased)', '', available, re.I)
    print type(result)
    print result
    pass


def test5():
    price = 'About 300 EURyuan'
    price = re.search(r'\S*? (\d*)', price, re.S)
    price = price.groups()[0]

    print "price:", price


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
