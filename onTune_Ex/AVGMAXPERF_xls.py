# coding=utf-8
# https://docs.python.org/3.4/library/xml.etree.elementtree.html
import psycopg2 as pg2
import xlsxwriter
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
e_date='2019-07-22 23:59:59'
fmt_date='%Y-%m-%d %H:%M:%S'

# print(datetime.strptime(s_date, fmt_date))
start_date=datetime.strptime(s_date, fmt_date)
end_date=datetime.strptime(e_date, fmt_date)
#next_date=datetime.strptime(s_date, fmt_date) + timedelta(seconds=600)
#next_date=datetime.strptime(s_date, fmt_date) + timedelta(minutes=10)
#next_date=datetime.strptime(s_date, fmt_date) + timedelta(hours=1)
#next_date=datetime.strptime(s_date, fmt_date) + timedelta(days=1)
print(start_date)
print(end_date)

next_date = start_date + timedelta(minutes=10)
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
FROM avgmaxperf_19072200 amp, hostinfo hi
WHERE amp._agentid=hi._agentid
"""
sql_avgmaxperf += "AND (to_timestamp(_ontunetime)::timestamp + '-9 hours' >= '" + start_date.strftime(fmt_date) + "') \n"
sql_avgmaxperf += "AND (to_timestamp(_ontunetime)::timestamp + '-9 hours' < '" + next_date.strftime(fmt_date) + "') \n"
sql_avgmaxperf += "group by hostname \n"

while next_date <= end_date:

    pre_date = next_date
    next_date = next_date + timedelta(minutes=10)
    print("next_date : " + next_date.strftime(fmt_date))

    sql_avgmaxperf += "union \n"
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
    FROM avgmaxperf_19072200 amp, hostinfo hi
    WHERE amp._agentid=hi._agentid
    """
    sql_avgmaxperf += "AND (to_timestamp(_ontunetime)::timestamp + '-9 hours' >= '" + pre_date.strftime(fmt_date) + "') \n"
    sql_avgmaxperf += "AND (to_timestamp(_ontunetime)::timestamp + '-9 hours' < '" + next_date.strftime(fmt_date)  + "') \n"
    sql_avgmaxperf += "group by hostname \n"


sql_avgmaxperf += ") \n"
sql_avgmaxperf += "SELECT * FROM avgmaxperf ORDER BY hostname, avgtime \n"
print(sql_avgmaxperf)

curs.execute(sql_avgmaxperf)

COLNM=['avgtime', 'avguser', 'avgsys', 'avgwait', 'avgmemused', 'savgwapused', 'avgdiskrw', 'avgnetworkrw']
print(COLNM)

outfile = "ontune_avgmaxperf.xlsx"
workbook=xlsxwriter.Workbook(outfile)  # type: object

xlrow = 1
hostname=""
for row_value in curs:
    if hostname == "" or hostname <> row_value[0]:
        hostname = row_value[0]
        sheetnm = "avgmaxperf_"+ hostname
        worksheet = workbook.add_worksheet(sheetnm)
        worksheet.write_row(0, 0, COLNM)

    worksheet.write_row(xlrow,0,row_value[1:])
    xlrow+=1
    print(xlrow)

print("Opened Database Successfully")
workbook.close()
conn.commit()

# 연결을 종료한다
curs.close()
conn.close()

