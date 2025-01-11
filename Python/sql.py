import sqlite3
a=sqlite3.connect('data.db')
b=a.cursor()
# '''b.execute('create table emp (ename varchar,empid number,esal number)')'''
b.execute('insert into emp values("ram",100,400000)')
b.execute('insert into emp values("abdul",101,500000)')
b.execute('insert into emp values("pinky",102,700000)')
b.execute('insert into emp values("john",103,900000)')
b.execute('insert into emp values("sai",104,400000)')
res=b.execute('select * from emp')
print(res.fetchall()[1][1])
a.commit()
a.close()



