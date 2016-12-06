# coding:utf-8
import MySQLdb
import string
import random

def create_cdk(num=1,digit=4):

    total_cdk = []
    for i in range(num):
        a=''
        for i in range(digit):
            s=random.choice(string.letters+string.digits)
            a+=s
        if a in total_cdk:
            num+=1
            continue   #如果出现相同的CDK 跳过添加，次数加1
        total_cdk.append(a.upper())
    return total_cdk


def insert_cdk(info,table='testtable'):
    db = MySQLdb.connect("localhost", "root", "1234", "testdb")
    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS testtable")

        cur.execute("CREATE TABLE IF NOT EXISTS \
            %s(Id INT PRIMARY KEY AUTO_INCREMENT, CDK VARCHAR(25))"%(table))

        try:
            for i in range(200):
                cur.execute('''INSERT INTO %s(CDK) VALUES('%s')'''%(table,info[i]))
            db.commit()
        except:
            db.rollback()

def get_cdk_from_table(num=1,table='testtable'):
    db = MySQLdb.connect("localhost", "root", "1234", "testdb")
    info =[]
    with db:
        cur = db.cursor()

        sql = "SELECT * FROM %s WHERE id < %d\
               "%(table,num+1)
        try:
            # 执行SQL语句
            cur.execute(sql)
            # 获取所有记录列表
            results = cur.fetchall()
            for row in results:
                cdk = row[1]
                info.append(cdk)



        except:
            print "Error: unable to fecth data"

    return info

if __name__ == '__main__':
    info = create_cdk(200,7)
    insert_cdk(info)
    s = get_cdk_from_table(4)
    print s