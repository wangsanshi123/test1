# -*- coding:utf-8 -*-
def fun1():
    pass
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L
if __name__ == '__main__':
    for i in fab(5):
        print i

    print fab(5)
    pass