import calendar

kr_base_holiday=['20171005','20171006','20171007']

def chk_holiday(yyyymmdd):
    yyyy,mm,dd=int(yyyymmdd[:4]),int(yyyymmdd[4:6],int(yyyymmdd[6:])
    if (yyyy>=2015 and yyyy<=2017):
        if kr_base_holiday.count(yyyymmdd):
            return True
        else:
            res=calendar.weekday(yyyy,mm,dd)
            if res == 5 or res == 6 :
                return True
    else:
        print("year is between 2016 ~ 2017 or 'ibk_dayutil.py ' file edit kr_base_holiday is values...")
        exit()

def month_busyday(yyyymm) :
    yyyy,mm=int(yyyymm[:4]),int(yyyymm[4:6])
    bd=[]
    d1=10
    d2=25
    month_end=calendar.monthrange(yyyy,mm)[1]
    for days in range(month_end,0,-1):
        if not check_holiday(yyyymm+str(days)):
            bd.append(days)

    while True:
        if d1 in bd:
            day1=d1
            break
        d1+=1

    while True:
        if d2 in bd:
            day2=d2
            break
        d2+=1

    return(yyyymm+str(d1),yyyymm+str(d2),yyyymm+str(bd[0])))