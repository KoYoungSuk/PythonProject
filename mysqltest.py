import pymysql as mysql

conn = mysql.connect(host='koyoungsuk2.iptime.org', user='kys', password='pw', db='dbstudent')

cur = conn.cursor()
cur.execute("select * from student")

for row in cur:
    print(row)