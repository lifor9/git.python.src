import PyMySQL
import time
import xlsxwriter
import calendar

TITLE = ['date']

conn = pymysql.connect(host='127.0.0.1', port=3306, user='ontune', passwd='ontune', db='ontunev3', charset='utf8')
curs = conn.cursor()

sql = "SELECT _agentid, _agentname FROM agentinfo WHERE _agentid != 0"
curs.execute(sql)

q1 = ""

for i in curs :
    q1 += """, MAX(CASE WHEN avgtable1._agentid={0} THEN avgtable1.avgcpu ELSE 0 END) AS '{0}_avgcpu' """.format(i[0])
    q1 += """, MAX(CASE WHEN maxtable1._agentid={0} THEN maxtable1.maxcpu ELSE 0 END) AS '{0}_maxcpu' """.format(i[0])
    q1 += """, MAX(CASE WHEN avgtable1._agentid={0} THEN avgtable1.avgmem ELSE 0 END) AS '{0}_avgmem' """.format(i[0])
    q1 += """, MAX(CASE WHEN maxtable1._agentid={0} THEN maxtable1.maxmem ELSE 0 END) AS '{0}_maxmem' """.format(i[0])

    TITLE.append("{0}_avgcpu".format(i[1]))
    TITLE.append("{0}_maxcpu".format(i[1]))
    TITLE.append("{0}_avgmem".format(i[1]))
    TITLE.append("{0}_maxmem".format(i[1]))

print(q1)

yyyy=2016
yy1="16"

for mm in range(1,9) :
    qyyddmm = []
    if len(str(mm)) == 1
        mm1 = "0{0}".format(str(mm))
    else :
        mm1 = str(mm)

    outfile = "ontunev4_0000_{0}.xlsx".format(mm1)
    xlrow = 1

    workbook = xlsxwriter.Workbook(outfile)


