# coding=utf-8
import psycopg2
import time
import datetime
import codecs

class Srvlist:
	def __init__(self,c1,c2,c3,c4,c5):
		self.dbip=c1
		self.dbport=c2
		self.dbuser=c3
		self.dbpw=c4
		self.dbname=c5
		#self.qd=d1
		#self.qdate="{0:04d}{1:02d}{2:02d}".format(self.qd.year, self.qd.month, self.qd.day)
		#self.qdate1 = "{0:04d}/{1:02d}/{2:02d}".format(self.qd.year, self.qd.month, self.qd.day)
		#self.qdate2 = "{0:2s}{1:02d}{2:02d}".format(str(self.qd.year)[-2:], self.qd.month, self.qd.day)

	def retcon(self):
		retdbconn=pymysql.connect(host=self.dbip, port=self.dbport, user=self.dbuser, passwd=self.dbpw, db=self.dbname, charset='utf8')
		return(retdbconn)

	def infoprtfile(self,rc1):
		for i in range(len(rc1)):
			#print(i, rc1[i][0], rc1[i][1], rc2[i][2], rc1[i][3], rc1[i][0], rc2[i][1], rc2[i][2], rc2[i][3])
			#f.write("{0},{1},{2},{3},{4},{5},{6},{7}\n".format(rc1[i][0], rc1[i][1], rc1[i][2], rc1[i][3], rc2[i][0], rc2[i][1], rc2[i][2], rc2[i][3]))
			f.write("{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(rc1[i][0], rc1[i][1], rc1[i][2], rc1[i][3], rc1[i][4], rc1[i][5], rc1[i][6], rc1[i][7], rc1[i][8]))
			#print(i,rc1[i][0], rc1[i][1], rc1[i][2], rc1[i][3], rc1[i][4], rc1[i][5], rc1[i][6], rc1[i][7])
		print(len(rc1))


class OntuneV3info(Srvlist):
	def __init__(self,c1,c2,c3,c4,c5,bd):
		Srvlist.__init__(self,c1,c2,c3,c4,c5)
		print("o3 ip=",self.dbip)
		self.sql0="create view h0 as select distinct(hostname) from realtimeperf{};".format(bd)
		self.sql1="SELECT hostname,ipaddress,model,sn,os,cpucount,cpuclock,memory,'{0}' FROM node WHERE hostname IN (SELECT hostname FROM h0);".format(self.dbip)
		self.sql2="drop view h0;"
		print(self.sql0)
		print(self.sql1)
	def query1(self):
		conn=Srvlist.retcon(self)
		cur=conn.cursor()
		cur.execute(self.sql0)
		cur.execute(self.sql1)
		curlist=list(cur)
		self.infoprtfile(curlist)
		cur.execute(self.sql2)
		cur.close()


class OntuneV4info(Srvlist):
	def __init__(self,c1,c2,c3,c4,c5,bd):
		Srvlist.__init__(self,c1,c2,c3,c4,c5)
		print("o4 ip=",self.dbip)
		self.sql0="""CREATE VIEW h0 AS SELECT DISTINCT(_agentid) FROM avgperf10_{0}00 UNION SELECT DISTINCT(_agentid) FROM avgperf1_{0}00 UNION SELECT DISTINCT(_agentid) FROM avgperf2_{0}00
UNION SELECT DISTINCT(_agentid) FROM avgperf3_{0}00 UNION SELECT DISTINCT(_agentid) FROM avgperf4_{0}00 UNION SELECT DISTINCT(_agentid) FROM avgperf5_{0}00
UNION SELECT DISTINCT(_agentid) FROM avgperf6_{0}00 UNION SELECT DISTINCT(_agentid) FROM avgperf7_{0}00 UNION SELECT DISTINCT(_agentid) FROM avgperf8_{0}00 UNION SELECT DISTINCT(_agentid) FROM avgperf9_{0}00;""".format(bd)
		self.sql1="SELECT a._agentname,a._ipaddress,a._model,a._serial,h._os,h._processorcount,h._processorclock,h._memorysize,'{0}' FROM agentinfo AS a, hostinfo AS h WHERE a._agentid IN (SELECT _agentid FROM h0) AND a._agentid=h._agentid".format(self.dbip)
		self.sql2="drop view h0;"
		#print(self.sql0)
		print(self.sql1)
	def query1(self):
		conn=Srvlist.retcon(self)
		cur=conn.cursor()
		cur.execute(self.sql0)
		cur.execute(self.sql1)
		curlist=list(cur)
		self.infoprtfile(curlist)
		cur.execute(self.sql2)
		cur.close()

if __name__ == '__main__':
	# bd = datetime.date(2017, 5, 28) 특정일자 지정의 경우
	bd=datetime.date.today()-datetime.timedelta(1)
	filename = "E:\\01_ontunedata_collect\\data\\{0}_ontune_info.csv".format("{0:04d}{1:02d}{2:02d}".format(bd.year, bd.month, bd.day))
	print(filename)
	qd="{0}{1:02d}{2}".format(str(bd.year)[-2:],bd.month, bd.day)
	qw=bd.weekday()+1
	if qw==7:
		qw=0
	print(qd)
	#f = open(filename, "w")
	f = codecs.open(filename, 'w',encoding='utf8')

	s1=OntuneV3info('134.100.207.27',18899,'ontuneadmin','&U*I9o0p','ontunev3',qw)
	s1.query1()
	s2=OntuneV3info('134.100.207.60',18899,'ontuneadmin','&U*I9o0p','ontunev3',qw)
	s2.query1()
	s3=OntuneV3info('134.100.207.101',18899,'ontuneadmin','&U*I9o0p','ontunev3',qw)
	s3.query1()

	s4=OntuneV4info('172.18.102.111', 18899, 'ontuneadmin', '&U*I9o0p', 'ontune',qd)
	s4.query1()
	s5 = OntuneV4info('172.18.102.112', 18899, 'ontuneadmin', '&U*I9o0p', 'ontune',qd)
	s5.query1()
	f.close()
