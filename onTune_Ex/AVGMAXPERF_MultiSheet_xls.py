# coding=utf-8
import psycopg2 as pg2
import xlrd
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

# datetime 변환, 계산
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
s_date='2019-07-22 00:00:00'
fmt_date='%Y-%m-%d %H:%M:%S'

# print(datetime.strptime(s_date, fmt_date))
start_date=datetime.strptime(s_date, fmt_date)

print(datetime.strftime(start_date, '%Y%m%d'))

next_date = start_date + timedelta(days=1)
print("next_date : " + next_date.strftime(fmt_date))

sql_avgmaxperf = "with avgmaxperf(hostname, avgtime, avguser, avgsys, avgwait, avgmemused, avgdiskrw, avgnetrw) as ( \n"
sql_avgmaxperf += """SELECT 
    _hostname as hostname,
    to_char(to_timestamp(min(_ontunetime))::timestamp + '-9 hours', 'YYYY-MM-DD HH24:MI:SS') as avgtime,
    round(avg(_user),2) as avguser,
    round(avg(_sys),2) as avgsys,
    round(avg(_wait),2) as avgwait,
    round(avg(_memoryused)/100,2) as avgmemused,
    round(avg(_swapused/100),2) as savgwapused,
    round(avg(_DiskReadWrite)/100,2) as avgdiskrw,
    round(avg(_NetworkReadWrite)/100,2) as avgnetworkrw      
FROM avgmaxperf_{0}00 amp, hostinfo hi
WHERE amp._agentid=hi._agentid
"""
sql_avgmaxperf += "AND (to_timestamp(_ontunetime)::timestamp + '-9 hours' >= '{1}') \n"
sql_avgmaxperf += "AND (to_timestamp(_ontunetime)::timestamp + '-9 hours' < '{2}') \n"
sql_avgmaxperf += "group by hostname "
sql_avgmaxperf += ") \n"
sql_avgmaxperf += "SELECT * FROM avgmaxperf ORDER BY hostname, avgtime \n"

print(sql_avgmaxperf.format(datetime.strftime(start_date, '%y%m%d'), start_date, next_date))

curs.execute(sql_avgmaxperf)

COLNM=['avgtime', 'avguser', 'avgsys', 'avgwait', 'avgmemused', 'savgwapused', 'avgdiskrw', 'avgnetworkrw']
print(COLNM)

outfile = "ontune_avgmaxperf.xlsx"
workbook = xlrd.open_workbook(outfile)
workbook.sheet_by_index(0)