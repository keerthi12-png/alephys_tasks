import mysql.connector as mysql

con = mysql.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="first"
)
cur = con.cursor()
cur.execute('select date,amount from sales')
result1=cur.fetchall()
print('data and amount')
for i in result1:
    print(i)
    print(' ')
cur.execute('select date, SUM(amount) FROM sales GROUP BY date ORDER BY date;')
print('Total Amount ')
result=cur.fetchall()
for row in result:
    print(row)
    print(' ')
con.close()


