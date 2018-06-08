# -*- coding:utf-8 -*-

from time import strftime, localtime, strptime, ctime, mktime, struct_time, time

import datetime


def test1():
    now = strftime("%Y-%m-%d %H-%M-%S", localtime())
    print now
    print localtime()
    pass


def test2():
    # last_update_sql < last_update
    last_update_sql = "2018-8-19"
    last_update = "2017-8-20"

    last_update_sql = strptime(last_update_sql, "%Y-%m-%d")
    last_update = strptime(last_update, "%Y-%m-%d")
    print last_update_sql
    print type(last_update_sql)
    print last_update_sql > last_update
    pass


def test3():
    str_time = "29 Jun 2017"
    # str_time = "29 3 2017"
    str_time = "2015, January"
    # str_time = strptime(str_time, "%d %b %Y")
    str_time = strptime(str_time, "%Y, %B")
    # print strftime("%Y-%m-%d", str_time)
    print strftime("%Y-%m", str_time)
    pass


def test4():
    date = 1418169600
    date = 1525773352305/1000
    dt = localtime(float(date))
    timeArray = strftime("%Y-%m-%d %H:%M:%S", dt)
    print timeArray


def test5(timestamp):
    # timestamp = 1474848000
    # timestamp = 1506498470
    # 转换成localtime
    time_local = localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = strftime("%Y-%m-%d %H:%M:%S", time_local)

    print dt


def test6():
    print ctime()
    print localtime()
    print localtime().tm_hour

    print localtime().tm_hour
    print localtime()[4]
    print  mktime(localtime())


def test7():
    "3 hrs 24 mins ago", "17 days ago"
    now = strftime("%Y-%m-%d %H-%M-%S", localtime())
    print now
    pass


def test8():
    d1 = datetime.datetime.strptime('2012-03-05 17:41:20', '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime('2012-03-02 15:41:20', '%Y-%m-%d %H:%M:%S')
    delta = d1 - d2
    print(delta)
    print delta.days
    print d1
    print type(d1)


def test9():
    now = datetime.datetime.today()
    delta = datetime.timedelta(days=3)
    print now
    print delta
    n_days = now + delta
    print n_days.strftime('%Y-%m-%d %H:%M:%S')


def parse():
    "3 hrs 24 mins ago", "17 days ago"
    days = 3
    hours = 2
    seconds = 1
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=days, hours=hours, seconds=seconds)
    n_days = now - delta
    print n_days.strftime('%Y-%m-%d %H:%M:%S')

    pass


def last_tddate():
    today = datetime.datetime.today().date()
    today = int(today.strftime("%w"))
    # if today == 0:
    #     return day_last_week(-2)
    # else:
    #     return day_last_week(-1)
    print today


def test10():
    t = strptime("2017-6-13", "%Y-%m-%d")
    y, m, d = t[0:3]
    date = datetime.datetime(y, m, d)
    print date
    print type(date)
    pass


def test11():
    announced = "2017, Sep"
    announced = announced.replace(" ", "")
    print announced
def test12():
    date ="2018-03-21 06:52 pm"
    date = strftime("%Y-%m-%d %H:%M", strptime(date, "%Y-%m-%d %I:%M %p"
                                                     "")) if date else ""
    print(date)
    pass



if __name__ == '__main__':
    # test1()
    # test2()
    test3()
    # test4()
    # test5(1506498470)
    # test5(1506498435)
    # test5(1506498435)
    # test6()
    # test7()
    # test8()
    # test9()
    # parse()
    # last_tddate()
    # test10()
    # test11()
    # test12()
    pass
