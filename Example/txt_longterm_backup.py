# coding=utf-8
import calendar

for mm in range(1,9):

    fname = "longterm_{0}{1}.txt".format('19', str(mm).zfill(2))
    f = open(fname, 'w')
    month_end = calendar.monthrange(2019,mm)[1]
    # print(month_end)
    bkstr = "pg_dump.exe --host localhost --port 5432 --username ontune --no-password  --format custom --blobs --verbose --file E:\onTuneBackup\LongTerm\L_20{0}{1}{2}00.backup  --table procargid_{0}{1}{2}00 --table avgperf_{0}{1}{2}00 --table avgvperf_{0}{1}{2}00 --table avgmaxperf_{0}{1}{2}00 --table avgpid_{0}{1}{2}00 --table avgproc_{0}{1}{2}00 --table avguserproc_{0}{1}{2}00 --table avgdisk_{0}{1}{2}00 --table avgnet_{0}{1}{2}00 --table avgadpt_{0}{1}{2}00 --table avglv_{0}{1}{2}00 --table avgvg_{0}{1}{2}00 --table avgmempool_{0}{1}{2}00 --table avgcpu_{0}{1}{2}00 --table avgdf_{0}{1}{2}00 --table scriptresult_{0}{1}{2}00 ontune"
    for dd in range(1, month_end+1):
        wbkstr = bkstr.format('19', str(mm).zfill(2), str(dd).zfill(2)) + "\n"
        f.write(wbkstr)

    f.close()



