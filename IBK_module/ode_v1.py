# coding=utf-8
import psycopg2
import time
import sys
import datetime


class Srvlist:
    def __init__(self, c1, c2, c3, c4, c5, d1):
        self.dbip = c1
        self.dbport = c2
        self.dbuser = c3
        self.dbpw = c4
        self.dbname = c5
        self.qd = d1
        self.qdate = "{0:04d}{1:02d}{2:02d}".format(self.qd.year, self.qd.month, self.qd.day)
        self.qdate1 = "{0:04d}/{1:02d}/{2:02d}".format(self.qd.year, self.qd.month, self.qd.day)
        self.qdate2 = "{0:2s}{1:02d}{2:02d}".format(str(self.qd.year)[-2:], self.qd.month, self.qd.day)

    def retcon(self):
        # retdbconn=pymysql.connect(host=self.dbip, port=self.dbport, user=self.dbuser, passwd=self.dbpw, db=self.dbname, charset='utf8')
        retdbconn = psycopg2.connect(database=self.dbname, user=self.dbuser, password=self.dbpw, host=self.dbip,
                                     port=self.dbport)
        return (retdbconn)

    def prtfile(self, rc1, rc2):
        print("len", len(rc1), len(rc2))
        if (len(rc1) == len(rc2) or len(rc1) > len(rc2)):
            for i in range(len(rc2)):
                # print(i, rc1[i][0], rc1[i][1], rc2[i][2], rc1[i][3], rc1[i][0], rc2[i][1], rc2[i][2], rc2[i][3])
                # f.write("{0},{1},{2},{3},{4},{5},{6},{7}\n".format(rc1[i][0], rc1[i][1], rc1[i][2], rc1[i][3], rc2[i][0], rc2[i][1], rc2[i][2], rc2[i][3]))
                f.write("{0},{1},{2},{3},{4},{5}\n".format(rc1[i][0], rc1[i][1], rc1[i][2], rc1[i][3], rc2[i][2],
                                                           rc2[i][3]))
        else:
            for i in range(len(rc1)):
                f.write("{0},{1},{2},{3},{4},{5}\n".format(rc1[i][0], rc1[i][1], rc1[i][2], rc1[i][3], rc2[i][2],
                                                           rc2[i][3]))


class OntuneV4(Srvlist):
    def __init__(self, c1, c2, c3, c4, c5, d1):
        Srvlist.__init__(self, c1, c2, c3, c4, c5, d1)
        print("o3 date=", self.qdate1, "o3 ip=", self.dbip)
        # self.sql1="select FROM_UNIXTIME(unixtime,'%Y/%m/%d %H:%i:%s') as yyyymmdd, hostname, if(round(pcrate/100,2)>100,100.00,round(pcrate/100,2)) as cpu, round(comp/100,2) as mem from ontunev3.avgperf{0} where FROM_UNIXTIME(unixtime,'%Y/%m/%d')='{1}' order by 2,1".format(
        #	self.qd.month - 1, self.qdate1)
        # self.sql2="select FROM_UNIXTIME(unixtime,'%Y/%m/%d %H:%i:%s') as yyyymmdd, hostname, if(round(pcrate/100,2)>100,100.00,round(pcrate/100,2)) as cpu, round(comp/100,2) as mem from ontunev3.maxperf{0} where FROM_UNIXTIME(unixtime,'%Y/%m/%d')='{1}' order by 2,1".format(
        #	self.qd.month - 1, self.qdate1)

        self.sql1 = """
					select 
						IF(hostname IN (SELECT hostname FROM wh), FROM_UNIXTIME(unixtime-32400,'%Y/%m/%d %H:%i:%s'), FROM_UNIXTIME(unixtime,'%Y/%m/%d %H:%i:%s')) as yyyymmdd, 
						hostname, 
						IF(round(pcrate/100,2)>100,100.00,round(pcrate/100,2)) as cpu, 
						round(comp/100,2) as mem 
					from ontune.avgperf{0} 
					where IF(hostname IN (SELECT hostname FROM wh), FROM_UNIXTIME(unixtime-32400,'%Y/%m/%d'), FROM_UNIXTIME(unixtime,'%Y/%m/%d')) = '{1}' order by 2,1
					""".format(self.qd.month - 1, self.qdate1)
        self.sql2 = """
					select 
						IF(hostname IN (SELECT hostname FROM wh), FROM_UNIXTIME(unixtime-32400,'%Y/%m/%d %H:%i:%s'), FROM_UNIXTIME(unixtime,'%Y/%m/%d %H:%i:%s')) as yyyymmdd, 
						hostname, 
						if(round(pcrate/100,2)>100,100.00,round(pcrate/100,2)) as cpu, 
						round(comp/100,2) as mem 
					from ontune.maxperf{0} 
					where IF(hostname IN (SELECT hostname FROM wh),FROM_UNIXTIME(unixtime-32400,'%Y/%m/%d'),FROM_UNIXTIME(unixtime,'%Y/%m/%d'))='{1}' 
					order by 2,1
					""".format(self.qd.month - 1, self.qdate1)

    def query1(self):
        conn = Srvlist.retcon(self)
        cura = conn.cursor()
        curm = conn.cursor()
        cura.execute(self.sql1)
        curm.execute(self.sql2)
        curalist = list(cura)
        curmlist = list(curm)
        self.prtfile(curalist, curmlist)
        cura.close()
        curm.close()


class OntuneV4(Srvlist):
    def __init__(self, c1, c2, c3, c4, c5, d1):

        Srvlist.__init__(self, c1, c2, c3, c4, c5, d1)
        print("o4 date=", self.qdate1, "o4 ip=", self.dbip)
        self.sql1 = []
        self.sql2 = []

        for groupnum in range(1, 11):
            sqlstr1 = """
					select 
						FROM_UNIXTIME(a._ontunetime-32400, '%Y/%m/%d %H:%i:%s') as yyyymmdd, 
						b._agentname, 
						if(a._user + a._sys + a._wait>100,100,a._user + a._sys + a._wait) as cpu , 
						if(round(a._memoryused / 100,2)>100, 100,round(a._memoryused / 100,2)) as mem 
					from avgperf{0}_{1}00 as a, agentinfo as b 
					where a._agentid=b._agentid
					""".format(groupnum, self.qdate2)

            self.sql1.append(sqlstr1)
            sqlstr2 = """
					select 
						FROM_UNIXTIME(a._ontunetime-32400, '%Y/%m/%d %H:%i:%s') as yyyymmdd, 
						b._agentname, if(a._usersyswait>100,100,a._usersyswait) as cpu, 
						if(round(a._memoryused / 100,2)>100, 100,round(a._memoryused / 100,2)) as mem 
					from avgmaxperf{0}_{1}00 as a, agentinfo as b 
					where a._agentid=b._agentid
					""".format(groupnum, self.qdate2)

            self.sql2.append(sqlstr2)

    def query1(self):
        conn = Srvlist.retcon(self)
        cura = conn.cursor()
        curm = conn.cursor()
        curalist = []
        curmlist = []
        for i1 in self.sql1:
            cura.execute(i1)
            curalist.extend(list(cura))
        for i2 in self.sql2:
            curm.execute(i2)
            curmlist.extend(list(curm))
        self.prtfile(curalist, curmlist)
        cura.close()
        curm.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        y = int(sys.argv[1][0:4])
        m = int(sys.argv[1][4:6])
        d = int(sys.argv[1][6:])
        bd = datetime.date(y, m, d)
    else:
        bd = datetime.date.today() - datetime.timedelta(1)
    #		print(sys.argv[1])
    #	else:
    #		print("nok")

    # bd=datetime.date.today()-datetime.timedelta(1)
    print("date : ", bd)
    filename = "E:\\{0}_ontune_perf_data.csv".format(
        "{0:04d}{1:02d}{2:02d}".format(bd.year, bd.month, bd.day))
    print(filename)
    f = open(filename, "w")

    #s1 = OntuneV3('134.100.207.27', 18899, 'ontuneadmin', '&U*I9o0p', 'ontunev3', bd)
    #s1.query1()
    #s2 = OntuneV3('134.100.207.60', 18899, 'ontuneadmin', '&U*I9o0p', 'ontunev3', bd)
    #s2.query1()
    #s3 = OntuneV3('134.100.207.101', 18899, 'ontuneadmin', '&U*I9o0p', 'ontunev3', bd)
    #s3.query1()

    s4 = OntuneV4('10.50.3.34', 5432, 'ontune', 'ontune', 'ontune', bd)
    s4.query1()
    s5 = OntuneV4('10.50.3.34', 5432, 'ontune', 'ontune', 'ontune', bd)
    s5.query1()
    f.close()
