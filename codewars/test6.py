# -*- coding:utf-8 -*-
from itertools import *
import math


def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    'I(1)V(5)X(10) L(50)C(100)    D(500)M(1000)'
    '''
        相同的数字连写，所表示的数等于这些数字相加得到的数，如 Ⅲ=3；
    小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 Ⅷ=8、Ⅻ=12；
    小的数字（限于 Ⅰ、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 Ⅳ=4、Ⅸ=9；
    在一个数的上面画一条横线，表示这个数增值 1,000 倍，如

=5000。
    '''
    'MCM－1900'
    'MCMLXXVI－1976'

    temp = ['I', 'X', 'C']
    dicts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    ls = []
    for item in roman:
        try:
            last = ls.pop()
        except:
            last = ''
            pass
        if last:
            sum += -dicts[last] if dicts[last] < dicts[item] and last in temp else dicts[last]
        ls.append(item)
        pass

    return sum + dicts[roman[-1]]

    pass


def solution2(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total


def recoverSecret(triplets):
    'triplets is a list of triplets from the secrent string. Return the string.'
    return ''.join(
        set([item[0] for item in triplets] + [item[1] for item in triplets] + [item[2] for item in triplets]))

    pass


def zeroes(base, number):
    def transform(base, number):
        if number == 0:
            return 0
        number = math.factorial(number)
        sum = ""
        while number >= base:
            sum += str(number % base)
            number = number / base

        sum += str(number)
        return sum[::-1]

    temp0 = transform(base, number % base)
    temp1 = transform(base, base) if number >= base else 0

    body = (number / base) * len(
        [item for item in takewhile(lambda x: x == 0, [int(item) for item in str(temp1)[::-1]]) if temp1 > 0])
    tail = len([item for item in takewhile(lambda x: x == 0, [int(item) for item in str(temp0)[::-1]]) if temp0 > 0])
    return body + tail

    pass


class Sudoku(object):
    # your code here
    [
        [7, 8, 4, 1, 5, 9, 3, 2, 6],
        [5, 3, 9, 6, 7, 2, 8, 4, 1],
        [6, 1, 2, 4, 3, 8, 7, 5, 9],

        [9, 2, 8, 7, 1, 5, 4, 6, 3],
        [3, 5, 7, 8, 4, 6, 1, 9, 2],
        [4, 6, 1, 9, 2, 3, 5, 8, 7],

        [8, 7, 6, 3, 9, 4, 2, 1, 5],
        [2, 4, 3, 5, 6,   1, 9, 7, 8],
        [1, 9, 5, 2, 8, 7, 6, 3, 4]
    ]



    def is_valid(self):
        '''       '''

        pass






if __name__ == '__main__':
    print zeroes(10, 10)
    print zeroes(10, 8)
    print zeroes(16, 16)

    print zeroes(8, 136)
    print zeroes(2, 10)

    pass
