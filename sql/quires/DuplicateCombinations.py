import mysql.connector as mysql

con = mysql.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="first"
)

cur = con.cursor()
cur.execute("SELECT * FROM transactions")
r = cur.fetchall()
print("All data in in table:")
for i in r:
    print(i)
cur.execute("""
    SELECT col1, col2, COUNT(*) AS duplicate_count
    FROM transactions
    GROUP BY col1, col2
    HAVING COUNT(*) > 1
""")
duplicates = cur.fetchall()

print("Duplicate (col1, col2) same transaction and their count:")
if duplicates:
    for row in duplicates:
        print(row)
else:
    print("✅ No duplicates found.")
con.close()
