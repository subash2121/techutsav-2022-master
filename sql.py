import sqlite3
con=sqlite3.connect('db.sqlite3')
cursor=con.cursor()
cursor.execute("select phno from user_profile where phno not in (select a.ph_number from techutsav_payment as a inner join user_profile as b on a.ph_number=b.phno) and department='CSE'")
rows=cursor.fetchall()
not_paid=[]
for row in rows:
    not_paid.append(row[0])
print(not_paid)
con.close()
