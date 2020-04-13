import psycopg2

# ================== Database Connection =================== st
conn_string = "host='192.168.15.50' dbname = 'ontune' user = 'ontune' password = 'ontune'"

try:
    conn = psycopg2.connect(conn_string)
    #conn = psycopg2.connect(database="ontune", user="ontune", password="ontune", host="10.50.3.34", port="5432")
except:
    print("error database connection")

curs = conn.cursor()
# ================== Database Connection =================== ed

TITLE = ['date']

agentlist = "SELECT _agentid, _agentname FROM agentinfo WHERE _agentid != 0"
curs.execute(agentlist)

query = ""


for i in curs :
    query += """, MAX(CASE WHEN avgtable1._agentid={0} THEN avgtable1.avgcpu ELSE 0 END) AS '{0}_avgcpu' """.format(i[0])
    query += """, MAX(CASE WHEN maxtable1._agentid={0} THEN maxtable1.maxcpu ELSE 0 END) AS '{0}_maxcpu' """.format(i[0])
    query += """, MAX(CASE WHEN avgtable1._agentid={0} THEN avgtable1.avgmem ELSE 0 END) AS '{0}_avgmem' """.format(i[0])
    query += """, MAX(CASE WHEN maxtable1._agentid={0} THEN maxtable1.maxmem ELSE 0 END) AS '{0}_maxmem' """.format(i[0])

    TITLE.append("{0}_avgcpu".format(i[1]))
    TITLE.append("{0}_maxcpu".format(i[1]))
    TITLE.append("{0}_avgmem".format(i[1]))
    TITLE.append("{0}_maxmem".format(i[1]))

print(query)