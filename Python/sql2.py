import sqlite3
a=sqlite3.connect('student.db')
b=a.cursor()
# b.execute('create table stu(sname varchar(20),sid number(5),scourse varchar(20))')
b.execute('insert into stu values("abrar",222,"CSE")')
b.execute('insert into stu values("hafeez",546,"EEE")')
res=b.execute('select * from stu')
print(res.fetchall())
# a.commit()
# a.close()

