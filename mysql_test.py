# -*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    db='stockinfo',
    # db='test',
)
cur = conn.cursor()


def test1():
    # 创建数据表
    # cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

    # 插入一条数据
    # cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
    # conn.commit()

    # 插入多条数据
    infos = [['501000', '2017-06-29', '3.184', '1.084', '1.084', '1.084', '100', '108'],
             ['501000', '2017-06-25', '2.982', '1.087', '1.082', '1.082', '166156', '179826']]

    # infos = [('501000', '2017-06-29', '1.084', '1.084', '1.084', '1.084', '100', '108'),
    #          ('501000', '2017-06-28', '1.087', '1.087', '1.082', '1.082', '166156', '179826')]
    infos = (['y', '1'], ['y', '1'])
    infos2 = (['yu', '1'], ['t', '1'])
    # cur.executemany('insert into baseinfo VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', infos)
    try:
        cur.executemany('insert into test1 VALUES (%s,%s)', infos)
    except BaseException, Argument:
        print Argument
        cur.executemany('insert into test1 VALUES (%s,%s)', infos2)

        pass
    conn.commit()


def test2():
    cur.execute("SELECT * FROM `gsmarena_phone` where `quote_author`='Force Majeure' ")
    dataset = cur.fetchall()
    # dataset = cur.fetchone()
    cur.close()
    conn.commit()
    print dataset


if __name__ == '__main__':
    # test1()
    test2()
