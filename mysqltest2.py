import pymysql as mysql


conn = mysql.connect(host="koyoungsuk2.iptime.org", user="kys", password="pw", db="dbstudent")

cur = conn.cursor()

sql = "insert into student values (%s, %s, %s)"
sql2 = "select * from student"
vals=("KoYoungSuk", "이과", "30702")
cur.execute(sql, vals)
print("success!")
cur.execute(sql2)
for row in cur:
    print(row)
conn.commit()
conn.close()