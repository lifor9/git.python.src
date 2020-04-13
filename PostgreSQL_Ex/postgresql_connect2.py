# coding=utf-8
import psycopg2

# 데이터베이스에 연결
conn = psycopg2.connect(database="ontune", user="ontune", password="ontune", host="10.50.3.34", port="5432")
# conn_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
#                 .format(dbname='ontune',
#                         user='ontune',
#                         host='10.50.3.34',
#                         password='ontune',
#                         port='5432')

#conn = psycopg2.connect(conn_string)

# 커서를 연다
cur = conn.cursor()

# CREATE TABLE 명령 실행
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Placeholder를 통해 데이터를 전달한다.
# placeholder는 어떤 데이터 타입의 경우에도 %s만 사용한다!!
# cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# SELECT명령을 실행해서 결과를 얻는다
cur.execute("SELECT * FROM agentinfo;")
print cur.fetchone()
#cur.fetchone()

# 데이터를 수정했을 경우 반드시 commit
conn.commit()

# 연결을 종료한다
cur.close()
conn.close()