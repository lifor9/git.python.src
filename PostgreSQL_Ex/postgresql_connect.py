# coding=utf-8
import psycopg2 as pg2

# ================== Database Connection =================== st
conn_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
                .format(dbname='ontune',
                        user='ontune',
                        host='10.50.3.34',
                        password='ontune',
                        port='5432')
try:
    conn = pg2.connect(database="ontune", user="ontune", password="ontune", host="10.50.3.34", port="5432")
    #conn = psycopg2.connect(conn_string)
except:
    print("error database connection")

curs = conn.cursor()

# ================== Database Connection ===================
sql_string = "SELECT * FROM agentinfo"
curs.execute(sql_string)
result = curs.fetchall()
print("Opened Database Successfully")


conn.commit()
