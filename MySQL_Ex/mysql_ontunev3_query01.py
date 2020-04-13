import pymysql
import time

def cpu_perf(qdate):
    conn = pymysql.connect(host='localhost', port=3306, user='ontune', password='ontune', db='ontune', charset='utf8')
    cur_avg = conn.cursor()
    cur_max = conn.cursor()

    hostgroup = []
    hostgroup.append("")
    hostgroup.append("(b._agentid in (51, 61, 71, 81, 91))")
    hostgroup.append("(b._agentid in (52, 62, 72, 92, 92))")

    SQLALL_MAX = """
    SELECT _ontunetime
    , MAX(CASE WHEN _agentname='pbihapa1' THEN _usersyswait ELSE 0 END) AS pbihapa1_cpumax
    FROM (SELECT _ontunetime, _agentname, _usersyswait FROM (
    """
    for gp in range(1, 11):
        hostgp = hostgroup[gp]
        SQL = "SELECT _ontunetime, b._agentname as _agentname, _usersyswait from avgmaxperf" + str(gp) + "_" + qdate[2:] + " a, agentinfo b where a._agentid=b._agentid and " + hostgp
        if gp ==10:
            SQLALL_MAX = SQLALL_MAX + SQL
        else:
            SQLALL_MAX = SQLALL_MAX + SQL + " union all "

    SQLALL_MAX = SQLALL_MAX + """
    ) AS maxtables ORDER BY _ontunetime, _agentname) AS realdata
    GROUP BY _ontunetime
    ORDER BY _ontunetime
    """

    SQLALL_AVG = """
    SELECT _ontunetime
    , MAX(CASE WHEN _agentname='pbihapa1' THEN _usersyswait ELSE 0 END) AS pbihapa1_cpuavg
    FROM (SELECT _ontunetime, _agentname, _usersyswait FROM (
    """

    for gp in range(1, 11):
        hostgp = hostgroup[gp]
        SQL = "SELECT _ontunetime, b._agentname as _agentname, _usersyswait from avgmaxperf" + str(gp) + "_" + qdate[2:] + " a, agentinfo b where a._agentid=b._agentid and " + hostgp
        if gp == 10:
            SQLALL_AVG = SQLALL_AVG + SQL
        else:
            SQLALL_AVG = SQLALL_AVG + SQL + " union all "

        SQLALL_AVG = SQLALL_AVG + """

    ) AS maxtables ORDER BY _ontunetime, _agentname) AS realdata
    GROUP BY _ontunetime
    ORDER BY _ontunetime
    """

    cur_max.execute(SQLALL_MAX)
    cur_avg.execute(SQLALL_MAX)
    cur_max.close()
    cur_avg.close()
    conn.close()
    return (cur_avg, cur_max)

def dfquery(EDATE, QDIR, MONDATE):
    conn = pymysql.connect(host='localhost', port=3306, user='ontune', password='ontune', db='ontune', charset='utf8')
    cur = conn.cursor()

    ANO = (1, 6)
    agentdata = []
    sqldata = ""
    EXTDIR = ""

    fstitle = []
    listdata = []
    endtablename = 'avgdf_{0}'.format(EDATE)

    for agentid in ANO:
        SQL = """SELECT
        REPLACE(agentinfo._agentname, CHAR(13), ''),
        REPLACE(dfnameid._name, CHAR(13), ''),
        REPLACE(lvnameid._name, CHAR(13), ''),
        {0}._totalsize, {0}._usage
        FROM {0}, dfnameid, lvnameid, agentinfo
        WHHERE {0}._agentid={1}
        and {0}._agentid = agentinfo._agentid
        and {0}._ontunetime = (SELECT MAX(_ontunetime) FROM {0} WHERE {0}._agentid={1}
        and {0}._dfnameid=dfnameid._id
        AND {0}._lvnameid=lvnameid._id
        """.format(endtablename, agentid)

        for DIRNAME in QDIR:
            SQL += " AND (dfnameid._name NOT LIKE '{0}%'".format(DIRNAME)

        cur.execute(SQL)

        cnt = 1

        for rr in cur:
            agentdata.append(rr)
            fdname = '{0}_{1}'.format(rr[0], rr[1])
            fsname1 = '{0}_{1}'.format(rr[0], cnt)
            cnt += 1
            fstitle.append(fsname)
            sqldata += " , max(case WHEN _agentid={0} and _dfname='{1}' THEN _uage ELSE 0 END) AS {2}\n".format(agentid, rr[1], fsname1)

    for DIRNAME in QDIR:
        EXTDIR += " AND dfnameid._name NOT LIKE '{0}'\n".format(DIRNAME)

    for mdate in MONDATE:
        SQLALL = """select _ontunetime {0} FROM (SELECT _ontunetime, _agentid, REPLACE(dfnameid._name, CHAR(13), '')
        _dfname, _usage FROM dfnameid, lvnameid, {1} WHERE (_ontunetime%300=0) AND (dfnameid._id = _dfnameid)
        AND (lvnameid._id = _lvnameid) AND _agentid IN {2} {3} ORDER BY _ontunetime) AS table1
        GROUP BY _ontunetime ORDER BY _ontunetime""".format(sqldata, mdate, ANO, EXTDIR)

        cur.execute(SQLALL)

        for rr in cur:
            d2 = time.strftime("%y/%m/%d, %H:%M:%S", time.localtime(int(rr[0]) - 32400))
            d1 = d2.split(sep=',')
            listdata.append(d1+list(rr[1:]))

    retdict = {'fstitle':fstitle, 'agentdata':agentdata, 'listdata':listdata}

    return retdict



