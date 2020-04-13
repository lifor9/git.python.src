# coding=utf-8
import psycopg2
import time
import sys

if len(sys.argv) == 1:
    exit(1)

m1 = str(sys.argv[1])

try:
    pgcon = psycopg2.connect(database="ontune", user="ontune", password="ontune", host="10.50.3.34", port="5432")
except:
    print("error database connection")

pgsql = """select a._ontunetime,b._agentname, a._user+a._sys ,c._user+c._sys 
	from  avgperf1_16"+m1+"2000 as a, agentinfo as b,avgmaxperf1_16"+m1+"2000 as c 
	where (a._agentid=c._agentid and a._ontunetime=c._ontunetime) and a._agentid=1 and a._agentid=b._agentid 
	order by  c._ontunetime 
	"""  # type: str

print pgsql
print "-------"
f = open("e:\\text1.txt", "w")

pgcur = pgcon.cursor()
pgcur = pgcon.execute(pgsql)

for result in pgcur:
    print time.strftime("%y/%m/%d %H:%M:%S", time.localtime(int(result[0]) - 32400)), result[1], result[2], result[3]
    data = str(time.strftime("%y/%m/%d %H:%M:%S", time.localtime(int(result[0]) - 32400))) + ";" + str(
        result[1]) + ";" + str(result[2]) + ";" + str(result[3]) + "\n"
    f.write(data)

f.close()
pgcon.close()
