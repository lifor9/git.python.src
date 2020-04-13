import psycopg2


# 데이터베이스에 연결
conn_string = "host='192.168.15.50' dbname = 'ontune' user = 'ontune' password = 'ontune'"
#conn_string = "database='testdb', user='ontune', password='ontune', host='127.0.0.1', port='5432'"

conn = psycopg2.connect(conn_string)
# conn = psycopg2.connect(database="ontune", user="ontune", password="ontune", host="10.50.3.34", port="5432")
print "Opened Database Successfully"

# Table 만들기
cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50) ,
       SALARY         REAL);''')

print "Table created successfully"

conn.commit()

# INSERT 조작
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 ) ");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 ) ");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 ) ");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 ) ");

conn.commit()
print "Records created successfully";

# SELECT 조작
cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = " , row[0]
   print "NAME = " , row[1]
   print "ADDRESS = " , row[2]
   print "SALARY = " , row[3], "\n"

print "Operation done successfully";

# UPDATE 조작
cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit
print "Total number of rows updated :" , cur.rowcount

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = " , row[0]
   print "NAME = " , row[1]
   print "ADDRESS = " , row[2]
   print "SALARY = " , row[3], "\n"

print "Operation done successfully";

# 삭제 작업
cur.execute("DELETE from COMPANY where ID=2;")
conn.commit
print "Total number of rows deleted :" , cur.rowcount

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = " , row[0]
   print "NAME = " , row[1]
   print "ADDRESS = " , row[2]
   print "SALARY = " , row[3], "\n"

print "Operation done successfully";

conn.close()

