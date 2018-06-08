# -*- coding:utf-8 -*-
def test1():
    str = 'yt...ytzhangyx'
    # str.strip("zhang")
    str = str.strip("yt...")
    print str
    pass


def test2():
    str = '''SweeT, 14 May 2017Disappointed...slow, bad cameras, bad software, bad speaker. I gave it away and bought a big S... morethat's what you paid for, that's what your money deserve, what more do you expect to some
kind of cheap devices???? a brilliant specs.? how could you! if I'll be the maker of this tablet and someone ask me to give such high specifications and expectations, I'll be asking you to pay double! that's why you need to th
ink before you do something you're uncertain ! fact hurts!
'''
    str1 = str.replace(
        '''SweeT, 14 May 2017Disappointed...slow, bad cameras, bad software, bad speaker. I gave it away and bought a big S... more''',
        "")
    print str1
    pass


def test3():
    announced = " ytx  tai xing "
    announced = announced.strip()
    # announced.strip()
    print announced


def test4():
    if 'yuan' is 'yuan':
        print "is"
    if 'yu' == 'yuan':
        print '=='
    if 'yu' is 'yuan' or'yuans':
        print 'is'
    if 'ta' == 'yuan' or'ta' is 'ta':
        print 'ta'


def test5():
    if 'yuan'.startswith('yu'):
        print 'yuan'

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()
    # test5()
