import operator


def persistence1(n):
    # your code
    time = 0

    while True:
        if len(str(n)) == 1:
            return time

        time += 1
        temp = [int(item) for item in str(n)]

        multi_result = 1
        for item in temp:
            multi_result *= item
        n = multi_result

    return time


def persistence2(n):
    number = 0
    while n >= 10:
        n = reduce(operator.mul, [int(item) for item in str(n)])
        number += 1

    return number

    pass

def test1():
    for i ,num in enumerate(str(3456)):
        print i,num,"\n"



if __name__ == '__main__':
    # print(persistence2(39))
    # print(persistence2(4))
    # print(persistence2(25))
    # print(persistence2(999))

    # print(persistence1(39))
    # print(persistence1(4))
    # print(persistence1(25))
    # print(persistence1(999))

    test1()
