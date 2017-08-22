# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

html_markup = '''<p class=”ecopyramid”>
<ul id=”producers”>
    <li class=”producerlist”>
        <div class=”name”>plants</div>
        <div class=”number”>100000</div>
    </li>
    <li class=”producerlist”>
        <div class=”name”>algae</div>
        Output in Beautiful Soup
        <div class=”number”>100000</div>
    </li>
</ul>'''
soup = BeautifulSoup(html_markup, 'lxml')
print(soup.prettify())
