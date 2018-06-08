# -*- coding:utf-8 -*-
s = 'hello'
a, b, c, d, e = s  # 将s[0]、s[1]……分别赋值给abcde
print a, b, c, d, e
a, _, _, _, e = s  # _只用下划线，默认为：要丢弃的变量，所以只有a，e赋值。
print a, e
print (a, e)

