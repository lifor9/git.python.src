# coding=utf-8
import sys


# rf = open('C:\Temp\eladisp_20191111_02.txt', 'rt')
# wf = open("C:\Temp\eladisp_20191111_02_fileter.txt", 'w')
rf = open('C:\Temp\metra2\eladisp_20191111_02.txt', 'rt')
wf = open("C:\Temp\metra2\eladisp_20191111_02_fileter.txt", 'w')

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

        line = rf.readline()
        # CSM Session Handle information
        line_split = line.split()
        csh_hex = line_split[2]
        csh_dec = line_split[3]

        line = rf.readline()
        line = rf.readline()
        line = rf.readline()
        # DOC ID
        line_split = line.split()
        doc_id = line_split[3]

        # dic_logs[inter_pid] = inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + obj_id + "," + errnm
        print(log_date + "," + inter_method + "," + exec_time + " sec, DOC ID : " + doc_id + ", CSM Session Handle : " + csh_hex + csh_dec + ", Network infomation : " + netid)
        wf.write(log_date + "," + inter_method + "," + exec_time + " sec, DOC ID : " + doc_id + ", CSM Session Handle : " + csh_hex + csh_dec + ", Network infomation : " + netid + "\n")

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

        line = rf.readline()
        line_split=line.split()
        # CSM Session Handle
        line_split = line.split()
        csh_hex = line_split[2]
        csh_dec = line_split[3]

        line = rf.readline()
        line_split=line.split()
        # CSM object Handle retrieved
        line_split = line.split()
        oh_hex = line_split[2]
        oh_dec = line_split[3]

        line = rf.readline()

        line = rf.readline()
        line_split=line.split()
        # read byte
        line_split = line.split()
        bytes_read = line_split[3]

        print(log_date + "," + inter_method + "," + exec_time + " sec, " + bytes_read_kb + " KB" + bytes_read + ", CSM Session Handle : " + csh_hex + csh_dec + ", CSM object Handle : " + oh_hex + oh_dec + ", Network infomation : " + netid)
        wf.write(log_date + "," + inter_method + "," + exec_time + " sec, " + bytes_read_kb + " KB" + bytes_read + ", CSM Session Handle : " + csh_hex + csh_dec + ", CSM object Handle : " + oh_hex + oh_dec + ", Network infomation : " + netid + "\n")

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

        line = rf.readline()
        line_split=line.split()
        # CSM Session Handle
        line_split = line.split()
        csh_hex = line_split[2]
        csh_dec = line_split[3]

        line = rf.readline()
        line_split=line.split()
        # CSM object Handle retrieved
        line_split = line.split()
        oh_hex = line_split[2]
        oh_dec = line_split[3]

        line = rf.readline()
        line = rf.readline()

        line = rf.readline()
        line_split=line.split()
        csum = line_split[3]

        print(log_date + "," + inter_method + "," + exec_time + " sec, CSM Session Handle : " + csh_hex + csh_dec + "," + oh_hex + oh_dec + ", csum : " + csum + ", Network infomation : " + netid)
        wf.write(log_date + "," + inter_method + "," + exec_time + " sec, CSM Session Handle : " + csh_hex + csh_dec + "," + oh_hex + oh_dec + ", csum : " + csum + ", Network infomation : " + netid + "\n")

        pre_line = line
        continue

    pre_line = line

rf.close()
wf.close()


