import PyMySQL
import time
import xlsxwriter

conn = pymysql.connect(host='127.0.0.1', port=3306, user='ontune', passwd='ontune', db='ontunev3', charset='utf8')
cur = conn.cursor()

sql01 = 'select  distinct hostname from nodeinfo'
cur.execute(sql01)

sql02 = "select avgtable1.yyyymmdd"
TITLE=['date']

for i in cur:
    sql02 +=", MAX(CASE WHEN avgtable1.hostname='{0}' THEN avgtable1.avgcpu ELSE 0 END) AS '{0}_avgcpu' \n".format(i[0])
    sql02 +=", MAX(CASE WHEN maxtable1.hostname='{0}' THEN maxtable1.maxcpu ELSE 0 END) AS '{0}_maxcpu' \n".format(i[0])
    sql02 +=", MAX(CASE WHEN avgtable1.hostname='{0}' THEN avgtable1.avgmem ELSE 0 END) AS '{0}_avgmem' \n".format(i[0])
    sql02 +=", MAX(CASE WHEN maxtable1.hostname='{0}' THEN maxtable1.maxmem ELSE 0 END) AS '{0}_maxmem' \n".format(i[0])

    TITLE.append("{0}_avgcpu".format(i[0]))
    TITLE.append("{0}_maxcpu".format(i[0]))
    TITLE.append("{0}_avgmem".format(i[0]))
    TITLE.append("{0}_maxmem".format(i[0]))

for i in range(8):
    xlrow = 1
    outfile = "ontunev3_{0}.xlsx".format(i)
    workbook = xlsxwriter.Workbook(outfile)
    worksheet = workbook.add_worksheet('month')

    print("query start time : ", time.ctime())

    sql03 = sql02 + """ from
            (select
                FROM_UNIXTIME(unixtime, '%Y/%m/%d') as yyyymmdd,
                hostname,
                round(AVG(usrsys+wait),2)  AS avgcpu,
                round(AVG(comp/100),2) AS avgmem
            from {0}
            group by hostname, FROM_UNIXTIME(unixtime, '%Y/%m/%d')) as avgtable1
            ,
            (select
                FROM_UNIXTIME(unixtime, '%Y/%m/%d') as yyyymmdd,
                hostname,
                MAX(usrsys+wait) AS maxcpu,
                MAX(comp/100) AS maxmem
            from {1}

    group by hostname, FROM_UNIXTIME(unixtime, '%Y/%m/%d')) as maxtable1
    where avgtable1.yyyymmdd=maxtable1.yyyymmdd and avgtable1.hostname=maxtable1.hostname
    group by avgtable1.yyyymmdd
    order by avgtable1.yyyymmdd, avgtable1.hostname""".format('avgperf{0}'.format(i), 'maxperf{0}'.format(i))

    worksheet.write_row(0,0,TITLE)

    cur.execute(sql03)

    for i in cur:
        worksheet.write_row(xlrow, 0, i)
        xlrow+=1

    print("query end time:", time.ctime())
    workbook.close()

