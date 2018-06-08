# -*- coding:utf-8 -*-
from lxml import etree

text = '''<table>
   <tbody>
   <tr>
       <td id = "tai">td11</td>
       <td id= "ytaixing">td12</td>
   </tr>
   <tr>
       <td>td21</td>
       <td>td22</td>
   </tr>
   </tbody>
   </table>'''

text2 = '''<table id="FundHoldSharesTable" class="table" cellspacing="0" cellpadding="0">
    <tbody>
    <tr class="">
        <td class="head">
            <div align="center">
                <strong>日期</strong>
            </div>
        </td>
    </tr>
    <tr class="gray">
        <td class="head">
            <div align="center">
                <strong>日期</strong>
            </div>
        </td>
    </tr>
    </tbody>
</table>'''
text3='''<table id="FundHoldSharesTable" class="table" cellspacing="0" cellpadding="0">
    <thead>
    <tbody>
    <tr class="">
        <td class="head">
            <div align="center">
                <strong>日期</strong>
            </div>
        </td>
        <td>
        <td>
        <td>
        <td class="tdr">
        <td class="tdr">
        <td class="tdr">
    </tr>
    <tr class="gray">
        <td class="head">
            <div align="center">
                <a target="_blank"
                   href="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehistory.php?symbol=sh600939&date=2017-06-30">
                    2017-06-30 </a>
            </div>
        </td>
        <td>
        <td>
        <td>
        <td class="tdr">
        <td class="tdr">
        <td class="tdr">
    </tr>
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
        <td class="head">
            <div align="center">
                <a target="_blank"
                   href="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehistory.php?symbol=sh600939&date=2017-06-23">
                    2017-06-23 </a>
            </div>
        </td>
        <td>
        <td>
        <td>
        <td class="tdr">
        <td class="tdr">
        <td class="tdr">
    </tr>
    <tr class="gray">
    <tr class="">
    <tr class="gray">
        <td class="head">
            <div align="center">
                <a target="_blank"
                   href="http://vip.stock.finance.sina.com.cn/quotes_service/view/vMS_tradehistory.php?symbol=sh600939&date=2017-06-20">
                    2017-06-20 </a>
            </div>
        </td>
        <td>
        <td>
        <td>
        <td class="tdr">
        <td class="tdr">
        <td class="tdr">
    </tr>
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    <tr class="gray">
    <tr class="">
    </tbody>
</table>'''


def test1():
    html = etree.HTML(text)
    # print html

    # results =  html.xpath(".//tr")
    # results = html.xpath(".//tr/td")
    # results = html.xpath("//table")
    results = html.xpath("//table")
    contents = results[0].xpath("string(.)").strip()
    print "type(contents)=========", type(contents)
    for result in results:
        print result.xpath("name()")
        # print result.string("//text()")


def test2():
    html = etree.HTML(text)
    results = html.xpath(".//*[contains(@id,'tai')]")
    for result in results:
        print result.xpath("name()")
        print result.xpath("number(123)")
        print result.xpath("text()")[0]

    pass


def test3():
    html = etree.HTML(text3)
    # results = html.xpath(".//*[@class='table']")
    results = html.xpath(".//*[@id='FundHoldSharesTable']")
    print results

    pass


if __name__ == '__main__':
    # test1()
    # test2()
    test3()
