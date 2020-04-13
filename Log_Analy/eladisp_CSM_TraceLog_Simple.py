# coding=utf-8
import sys


# rf = open('C:\Temp\eladisp_20191111_02.txt', 'rt')
# wf = open("C:\Temp\eladisp_20191111_02_fileter.txt", 'w')
rf = open('C:\Temp\metra1\ela_trace_20191111.txt', 'rt')
wf = open("C:\Temp\metra1\ela_trace_20191111_fileter_simple.txt", 'w')

# for line in rf:
while True:
    line = rf.readline()
    if not line: break

    if "CSM:OpenCsumObject" in line :
        line_split = line.split()
        # 호출 메소드 (CSM:OpenCsumObject)
        inter_method = line_split[1]
        log_date = line_split[2]
        exec_time = line_split[3]
        # bytes_read_kb = line_split[4]

        line = rf.readline()
        # NETWORK information
        line_split = line.split()
        netid = line_split[2]

        # dic_logs[inter_pid] = inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + obj_id + "," + errnm
        print(log_date + "," + inter_method + "," + exec_time + " sec, Network infomation : " + netid)
        wf.write(log_date + "," + inter_method + "," + exec_time + " sec, Network infomation : " + netid + "\n")

        pre_line = line
        continue

    if "CSM:ReadObject" in line :
        line_split = line.split()
        # 호출 메소드 (CSM:OpenCsumObject)
        inter_method = line_split[1]
        log_date = line_split[2]
        exec_time = line_split[3]
        bytes_read_kb = line_split[5]

        line = rf.readline()
        # NETWORK information
        line_split = line.split()
        netid = line_split[2]

        print(log_date + "," + inter_method + "," + exec_time + " sec, " + bytes_read_kb + " KB" + ", Network infomation : " + netid)
        wf.write(log_date + "," + inter_method + "," + exec_time + " sec, " + bytes_read_kb + " KB" + ", Network infomation : " + netid + "\n")

        pre_line = line
        continue

    if "CSM:CloseCsumObject" in line:
        line_split = line.split()
        # 호출 메소드 (CSM:CloseCsumObject)
        inter_method = line_split[1]
        log_date = line_split[2]
        exec_time = line_split[3]
        # bytes_read_kb = line_split[4]

        line = rf.readline()
        # NETWORK information
        line_split = line.split()
        netid = line_split[2]

        print(log_date + "," + inter_method + "," + exec_time + " sec, Network infomation : " + netid)
        wf.write(log_date + "," + inter_method + "," + exec_time + " sec, Network infomation : " + netid + "\n")

        pre_line = line
        continue

    pre_line = line

rf.close()
wf.close()


