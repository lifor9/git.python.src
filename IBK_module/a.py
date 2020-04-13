import sys
import datetime

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if len(sys.argv[1])==8:
            y = int(sys.argv[1][0:4])
            m = int(sys.argv[1][4:6])
            d = int(sys.argv[1][6:])
            bd = datetime.date(y, m, d)
        else:
            print("retry")
            print("ex: ",sys.argv[0],"20190709")
            exit()
    else:
        bd = datetime.date.today() - datetime.timedelta(1)

    print(bd)
# else:
#		print("nok")
# bd = datetime.date(y,m,d)
# print(bd)
