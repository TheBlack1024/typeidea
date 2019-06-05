
#coding=utf-8
#RDBMS特点
#1.数据以表格形式出现
#2.每行为各种记录名称
#3.每列为记录名称所对应的数据域
#4.许多的行和列组成一个表单
#5.若干的表单组成database



import pymysql

def select(table_name):
    #链接数据库
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="mysql123",db="test1")
    cur = conn.cursor()#获取主键光标

    #查询
    sql1 = "select * from {0}".format(table_name)
    reCount = cur.execute(sql1)#返回受影响的行数
    #print(reCount)
    data = cur.fetchall()#返回数据，返回的是tuple类型
    for i in data:
        print(i)

    cur.close()
    conn.close()
    return data
def insert(table_name):
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="mysql123",db="test1")
    cur = conn.cursor()

    #插入数据
    sql2 = "insert into {0}(name,password) values(%s,%s)".format(table_name)
    params = ("wangwu","123567")
    reCount = cur.execute(sql2,params)

    #批量插入数据
    li =[("zhaoda","852963"),("qinfei","789654")]
    sql3 = "insert into {0}(name,password) values(%s,%s)".format(table_name)
    reCount = cur.executemany(sql3,li)

    conn.commit()

    cur.close()
    conn.close()

def delete(table_name):
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="mysql123",db="test1")
    cur = conn.cursor()

    #删除数据
    list = select(table_name)
    #list = ["zhangsan", "lisi", "wangwu", "zhaoda", "qinfei"]
    for i in list:
        sql4 = "delete from {0} where name = '{1}'".format(table_name,i[1])
        reCount = cur.execute(sql4)

    conn.commit()
    cur.close()
    conn.close()



def update(table_name):
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="mysql123",db="test1")
    cur = conn.cursor()

    #更改数据
    list = select(table_name)
    #list = ["zhangsan","lisi","wangwu","zhaoda","qinfei"]
    a = 1
    for i in list:
        sql5 = "update {0} set id='{1}' where name='{2}'".format(table_name,a,i[1])
        reCount = cur.execute(sql5)
        a += 1

    conn.commit()
    cur.close()
    conn.close()

def alter_drop(table_name):
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="mysql123",db="test1")
    cur = conn.cursor()

    #删除字段（列）
    sql6 = "alter table {0} drop password".format(table_name)
    cur.execute(sql6)

    conn.commit()

    cur.close()
    conn.close()

def alter_add(table_name):
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="mysql123",db="test1")
    cur = conn.cursor()

    #添加字段（列）
    sql7 = "alter table {0} add id int(8) not null".format(table_name)
    cur.execute(sql7)

    conn.commit()

    cur.close()
    conn.close()


#insert("student")
#update("student")
select("student")










