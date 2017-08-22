# -*- coding:utf-8 -*-
def listToTuple():
    list_temp = [1, 2, 3, 4, 5, 4, 7]
    if 1 in list_temp:
        print "exist"

    # print list_1.index(5)
    # print list_1.index(6)
    print tuple(list_temp)


def list_delete():
    list_temp = [1, 2, 3, 4]
    pop = list_temp.pop(0)
    print list_temp
    print pop


def list_test1():
    list_temp = [2, 5, 7, 8]
    list_temp2 = [str(i) for i in list_temp]
    # print [str(i) for i in list_temp]
    print list_temp2


def list_assign():
    list_temp = [2, 5, 7, 8]
    list_temp2 = list_temp
    print list_temp2
    list_temp.pop()
    print list_temp2


def list_copy():
    '浅拷贝'
    list_temp = [2, 5, 7, 8]
    list_temp2 = list_temp[0:2]
    list_temp = list_temp[0:2]
    print list_temp2
    print list_temp


if __name__ == '__main__':
    # list_delete()
    # list_test1()
    # list_assign()
    list_copy()
