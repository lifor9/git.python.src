# coding=utf-8
import psycopg2 as pg2
import xlsxwriter
import calendar
import os
from datetime import datetime, timedelta


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

# 엑셀 컬럼 정의
sql_hostinfo = "SELECT _agentid, _hostname FROM hostinfo ORDER BY _agentid"
curs.execute(sql_hostinfo)

COLNM=['DATE']
for hn in curs:
    COLNM.append("{0}_AVGCPU".format(hn[1]))
    COLNM.append("{0}_AVGMEM".format(hn[1]))
    COLNM.append("{0}_MAXCPU".format(hn[1]))
    COLNM.append("{0}_MAXMEM".format(hn[1]))

print(COLNM)

outfile = "ontune_month_avgmaxperf.xlsx"
if os.path.isfile(outfile):
    print("파일이 존재 : " + os.path.abspath(outfile))
    os.remove(os.path.abspath(outfile))

workbook = xlsxwriter.Workbook(outfile)  # type: object
for mm in range(7,8):
    xlrow = 1
    worksheet = workbook.add_worksheet(str(mm).zfill(2))
    worksheet.write_row(0,0,COLNM)
    month_end = calendar.monthrange(2019,mm)[1]
    # print(month_end)
    sql_perf = "WITH T_MONTH_PERF(ontunedate, hostname, avgcpu, avgmem, maxcpu, maxmem) AS ("
    for dd in range(1, month_end+1):
        sql_perf = sql_perf + """
            SELECT 
                (to_timestamp(ap._ontunetime)::timestamp + '-9 hours')::date as ontunedate,
                hi._hostname as hostname,
                round(avg(ap._user+ap._sys+ap._wait),2) as avgcpu,
                round(avg(ap._memoryused/100),2) as avgmem,
                round(max(amp._usersyswait),2) as maxcpu,
                round(max(amp._memoryused)/100,2) as maxmem 
            FROM avgperf_19{0}{1}00 ap, avgmaxperf_19{0}{1}00 amp, hostinfo hi
            WHERE ap._agentid = hi._agentid
            AND amp._agentid=hi._agentid
            group by ontunedate, hostname
        """.format(str(mm).zfill(2), str(dd).zfill(2))
        if dd != month_end :
            sql_perf = sql_perf + "UNION"
        else:
            sql_perf = sql_perf + ") SELECT ontunedate, avgcpu, avgmem, maxcpu, maxmem FROM T_MONTH_PERF ORDER BY ontunedate, hostname"
    # print(sql_perf)

    try:
        curs.execute(sql_perf)
        for cur in curs:
            worksheet.write_row(xlrow, 0, cur)
            xlrow += 1
    except Exception as e:
        print(e)
        raise e
    finally:
        # 연결을 종료한다
        workbook.close()
        curs.close()
        conn.close()
