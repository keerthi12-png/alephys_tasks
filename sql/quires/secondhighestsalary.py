import mysql.connector as mysql


con = mysql.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="first"
)
cur = con.cursor()
cur.execute("select salary from employees")
result=cur.fetchall()

print("All salaries from the user")
for i in result:
    print(i)
    print('\n')
    
cur.execute("select MAX(salary) from employees where  salary<(select Max(salary) from employees)");

value1=cur.fetchone()
print('secound max salary',value1)

con.close()
