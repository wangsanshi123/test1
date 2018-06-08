# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

# soup = BeautifulSoup(open('test1.html'), 'lxml', from_encoding='utf-8')
soup = BeautifulSoup(open('temp.html'), 'lxml', from_encoding='utf-8')
# print soup.a
# print soup.a['href']
# print soup.a['param']
# print soup.a.attrs
# print soup.a.string
# print soup.head.contents
# print soup.head.string
# print soup.title.string
# print soup.a.string
# print soup.a.strings

# for string in soup.a.strings:
#     print string
#

# for string in soup.stripped_strings:
#     print string



# for a in soup.a.next_siblings:
#     print a.string.strip()
# print soup.a.next_sibling
# print soup.a.next_sibling.next_sibling



#搜索文档树
