# coding=utf-8
import calendar

addunixtime = 0
for mm in range(1,9):

    fname = "avglv_{0}{1}_286.sql".format('19', str(mm).zfill(2))
    f = open(fname, 'w')
    month_end = calendar.monthrange(2019,mm)[1]
    # print(month_end)

    insert_sql = "INSERT INTO avglv_{0}{1}{2}00 \n"
    # select_sql = "SELECT _ontunetime+31536000,_agenttime+31536000,"
    # select_sql = select_sql + "_agentid,_ionameid,_descid,_readrate,_writerate,_readiops,_writeiops,_readtime,_writetime "
    # select_sql = select_sql + "FROM avglv_{0}{1}{2}00 "
    # select_sql = select_sql + "WHERE _agentid in ({3}) ORDER BY _ontunetime; \n"
    select_sql = "SELECT _ontunetime+{0},_agenttime+{0},"
    select_sql = select_sql + "286,_ionameid,_descid,_readrate,_writerate,_readiops,_writeiops,_readtime,_writetime "
    select_sql = select_sql + "FROM avglv_1803{1}00 "
    select_sql = select_sql + "WHERE _agentid in ({2}) ORDER BY _ontunetime; \n"

    unixtime = 26438400 + addunixtime
    print(unixtime)

    for dd in range(1, month_end+1):
        # wbkstr = insert_sql.format('19', str(mm).zfill(2), str(dd).zfill(2)) + select_sql.format('18', str(mm).zfill(2), str(dd).zfill(2), '220,221')
        wbkstr = insert_sql.format('19', str(mm).zfill(2), str(dd).zfill(2)) + select_sql.format(str(unixtime),str(dd).zfill(2),'142')
        addunixtime = addunixtime + 86400
        f.write(wbkstr)
        if mm == 8 and dd == 20:
            break

    f.close()



