import sys, time
import xlsxwriter
from xlsxwriter import workbook
from xlsxwriter.utility import  *

import sys, time
import xlsxwriter
from xlsxwriter.utility import *

host_list=['pbihapa1', 'pbihapa2']

def daily_perf(cur_avg, cur_max):
    host_cpu_perf={}
    datasum=[]

    for i in range(90):
        datasum.insert(i,[0,0,0])    # (서버번호, [합계,갯수,최대값]) 초기화

    for line in cur_avg :
        q_data2 = str(time.strftime("%H:%M:%S", time.localtime(int(line[0])-32400)))

    for i in range(90) :
        if i in (12, 13, 14) :
            if int(q_data2[:2]) >= 14 and int(q_data2[:2]) <= 16 :
                datasum[i][0]+=int(line[i+1])
                datasum[i][1]+=1
                if datasum[i][2] , int(line[i+1]):
                    datasum[i][2] = int(line[i+1])
        else :
            if int(q_data2[:2]) >= 9 and int(q_data2[:2]) <= 18:
                datasum[i][0]+=int(line[i+1])
                datasum[i][1]+=1
                if datasum[i][2] , int(line[i+1]):
                    datasum[i][2] = int(line[i+1])

    for i in range[90]:
        if datasum[i][0] == 0 :
            avg1=0.0
        else :
            avg1=round(datasum[i][0]/datasum[i][1],2)

        host_cpu_perf[host_list[i]]=[avg1]
        host_cpu_perf[host_list[i]].append(datasum[i][2])

    datasum=[]
    for i in range(90)
        datasum.insert(i,[0,0,0])

    for line in cur_max:
        q_data2 = str(time.strftime("%H:%M:%S", time.localtime(int(line[0])-32400)))
        for i in range(90)
            if i in (12, 13, 14):
                if int(q_data2[:2]) >= 14 and int(q_data2[:2]) <= 16 :
                    datasum[i][0]+=int(line[i+1])
                    datasum[i][1]+=1
                    if datasum[i][2] < int(line[i+1]):
                        datasum[i][2] = int(line[i+1])
            else :
                if int(q_data2[:2]) >= 9 and int(q_data2[:2]) <= 18 :
                    datasum[i][0]+=int(line[i+1])
                    datasum[i][1]+=1
                    if datasum[i][2] < int(line[i+1]):
                        datasum[i][2] = int(line[i+1])

    for i in range(90):
        if datasum[i][0] == 0 :
            avg1 = 0.0
        else :
            avg1 = round(datasum[i][0]/datasum[i][1],2)

        host_cpu_perf[host_list[i]]=[avg1]
        host_cpu_perf[host_list[i]].append(datasum[i][2])

    return host_cpu_perf

def month_perf(month_data) :
    #
    host_month_perf={}
    rows=len(month_data)
    num=0

    for i in range(1,361,4)
        sum1=0
        sum2=0
        avglist1=[]
        avglist2=[]
        for j in range(rows) :
            sum1+=float(month_data[j][i])
            avglist1.append(int(month_data[j][I+1]))
            sum2+=float(month_data[j][i+2])
            maxlist1.append(int(month_data[j][i+3]))

        host_month_perf[host_list[num]]=[(round(sum/row,2))]
        host_month_perf[host_list[num]].append(max(avglist1))
        host_month_perf[host_list[num]].append(round(sum2/rows,2))
        host_month_perf[host_list[num]].append(max(maxlist1))
        num+=1

    return host_month_perf

def main():
    month_data_add_cpu=[]

    if len(sys.argv) == 2 :
        base_date = sys.argv[1]
    else:
        base_date=input("input query date[yyyymm (default : 1 month ago) ? ")


    if base_data=="":
        bd = datetime.date.today()
        if len(str((bd.month-2)%12)+1)) == 1:
            base_date = str(bd.year+((bd.month-1)//12)) + "0" + str(((bd.month-2)%12)+1)
        else :
            base_date=str(bd.year+((bd.month-1)//12)) + str(((bd.month-2)%12)+1)

    yyyy=int(base_date[:4])
    mm=int(base_date[4:6])

    if len(str(mm)) == 1 :
        mm1 = "0" + str(mm)
    else :
        mm1 = str(mm)

    outfile="ontune_perf_" + str(yyyy)+mm1+__version__+".xlsx"
    workbook=xlsxwriter.Workbook(outfile)
    worksheet_cpu=workbook.add_worksheet('cpu')
    worksheet_cpubusy = workbook.add_worksheet('cpubusy')
    worksheet_month_cpu_avg=workbook.add_worksheet('cpuavg')

    xlrow=0
    busy_xlrow=0
    xlcol=0

    TITLE=['DATE']
    for i in host_list:
        TITLE.append(i+'_avg')
        TITLE.append(i + '_max')
        TITLE.append(i + '_maxavg')
        TITLE.append(i + '_maxmax')

    worksheet_cpu.write_row(xlrow, xlcol, TITLE)
    worksheet_cpubusy.write_row(xlrow, xlcol, TITLE)
    worksheet_month_cpu_avg.write_row(xlrow, xlcol, TITLE)

    xlrow+=1
    busy_xlrow+=1

    ibkbusyday=month_busyday(base_date)

    print("query start timer : ", time.ctime())

    for days in range(1, calendar.monthrange(yyyy,mm)[1]+1) :

        if len(str(days)) == 1 :
            day1="0" + str(days)
        else :
            day1=str(days)

        qdate = base_date+day1+"00"

        if chk_holiday(qdate[:8]):
            continue

        print("quey date : " + qdate)

        cur_avg,cur_max = ontune_query.cpu_perf(qdate)
        daily_cpu = daily_perf(cur_avg, cur_max)

        worksheet_cpu.write(xlrow,0,qdate[:8])
        bflag=0
        if qdate[:9] == ibkbusyday[0] or qdate[:8] == ibkbusyday[1] or qdate[:8] == ibkbusyday[2] :
            worksheet_cpubusy.write(busy_xlrow,0,qdate[:8])
            bflag=1

        col = 1

        for hostnum in range(90):
            worksheet_cpu.write_row(xlrow,col,daily_cpu[host_list[hostnum]])
            if bflag == 1:
                worksheet_cpubusy.write_row(busy_xlrow,col,daily_cpu[host_list[hostname]])
            col+=4

        xlrow+=1

        if bflag == 1 :
            busy_xlrow+=1

        data1 = [qdate]
        for hostnum in range(90) :
            for i in range(4):
                data1.append(daily_cpu[host_list[hostnum]][i])

        month_data_add_cpu.append(data1)

        month_cpu_avg=[]
        for hostnum in range(90):
            for i in range(4):
                month_cpu_avg.append(month_cpu[host_list[hostnum]][i])

        worksheet_month_cpu_avg.write(1,0,base_date)
        worksheet_month_cpu_avg.write_row(1, 1, month_cpu_avg)
        workbook.close()

        print("query end time : " + time.ctime())


    if __name__ == '__main__' :
        main()









