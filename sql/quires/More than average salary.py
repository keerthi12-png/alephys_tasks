import mysql.connector as mysql


con = mysql.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="first"
)
cur = con.cursor()
cur.execute("select salary from employees ")
result=cur.fetchall()

print("All salaries from the user")
for i in result:
    print(i)
    print('\n')
    
cur.execute(""" SELECT emp_id, emp_name, department, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
)
ORDER BY department, salary DESC;""")

value1=cur.fetchone()
print('More than average salary in the department',value1)
con.close()

