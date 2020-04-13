# coding=utf-8
import psycopg2 as pg2
import time

def cpu_perf(qdata):
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

    cur_avg = conn.cursor()
    cur_max = conn.cursor()

    hostgroup = []
    hostgroup.append("")
    # ================== Database Connection ===================

