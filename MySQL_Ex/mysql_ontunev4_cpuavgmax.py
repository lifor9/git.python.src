import PyMySQL
import time
import xlsxwriter
import calendar

TITLE=['data']
conn = pymysql.connect(host='127.0.0.1', port=3306, user='ontune', passwd='ontune', db='ontunev3', charset='utf8')
cur = conn.cursor()

########################################################################################################################
sql="select _agentid, _agentname from agentinfo where _agentid != 0"
cur.execute(sql)

q1=""

for i in cur:
    q!+=""", MAX(CASE WHEN avgtable1._agentid={0} THEN avgtable1.avgcpu ELSE 0 END) AS '{0}_avgcpu'
    ,  MAX(CASE WHEN maxtable1._agentid={0} THEN maxtable1.maxcpu ELSE 0 END) AS '{0}_maxcpu'
    ,  MAX(CASE WHEN avgtable1._agentid={0} THEN avgtable1.avgmem ELSE 0 END) AS '{0}_avgmem'
    ,  MAX(CASE WHEN maxtable1._agentid={0} THEN maxtable1.maxmem ELSE 0 END) AS '{0}_maxmem'
    """.format(i[0])

    TITLE.append("{0}_avgcpu".format(i[1]))
    TITLE.append("{0}_maxcpu".format(i[1]))
    TITLE.append("{0}_avgmem".format(i[1]))
    TITLE.append("{0}_maxmem".format(i[1]))

print(TITLE)
########################################################################################################################

yyyy=2016
yy1="16"

for mm in range(1,9):
    qyyddmm = []
    if len(str(mm)) == 1:
        mm1 = "0{0}".format(str(mm))
    else :
        mm1 = str(mm)

    outfile = "ontunev4_{0}.xlsx".format(mm1)
    xlrow=1
    workbook = xlsxwriter.Workbook(outfile)
    worksheet = workbook.add_worksheet('month')
    worksheet.write_row(0,0,TITLE)
    month_end=calendar.monthrange(yyyy,mm)[1]

    for dd in rang(1, month_end+1) :
        if len(str(dd)) == 1:
            dd1="0{0}".format(str(dd))
        else :
            dd1 = str(dd)

        qyyddmm.append('{0}{1}{2}'.format(yy1,mm1,dd1))

    for qdate in qyyddmm :
        sql="select avgtable1.yyyymmdd " + q1 + " from "
        sql1=""" (
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf10_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf1_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf2_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf3_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf4_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf5_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf6_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf7_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf8_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(AVG(_user + _sys + _wait), 2)  AS avgcpu, round(AVG(_memoryused / 100), 2) AS avgmem from avgperf9_{0}00 group by _agentid
            ) as avgtable1, """.format(qdate)

        sql2=""" (
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf10_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf1_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf2_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf3_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf4_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf5_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf6_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf7_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf8_{0}00 group by _agentid
            union all
            select FROM_UNIXTIME(_ontunetime-32400, '%Y/%m/%d') as yyyymmdd, _agentid, round(MAX(_user + _sys + _wait), 2) AS maxcpu, round(MAX(_memoryused / 100), 2) AS maxmem from avgmaxperf9_{0}00 group by _agentid
            ) as maxtable1 """.format(qdate)

    sql=sql+sql1+sql2
    sql+="""
        where avgtable1.yyyymmdd=maxtable1.yyyymmdd and avgtable1._agentid=maxtable1._agentid
        group by avgtable1.yyyymmdd
        order by avgtable1.yyyymmdd, avgtable1._agentid
    """
    try :
        cur.execute(sql)

        for i in cur :
            worksheet.write_row(xlrow, 0, i)
            xlrow+=1
            print(i[0])
    except :
        pass

    workbook.close()