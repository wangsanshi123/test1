from time import strftime, localtime, strptime


def test1():
    now = strftime("%Y-%m-%d %H-%M-%S", localtime())
    print now
    pass


def test2():
    # last_update_sql < last_update
    last_update_sql = "2017-8-21"
    last_update = "2017-8-20"

    last_update_sql = strptime(last_update_sql, "%Y-%m-%d")
    last_update = strptime(last_update, "%Y-%m-%d")
    print type(last_update_sql)
    print last_update_sql > last_update
    pass


if __name__ == '__main__':
    # test1()
    test2()
