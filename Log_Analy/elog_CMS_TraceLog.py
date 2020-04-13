# coding=utf-8
import sys

# if __name__ == "__main__":
# args = sys.argv[1:]
# for i in args:
#     print(i)


# rf = open('C:\Temp\elog20191111', 'rt')
# wf = open("C:\Temp\elog20191111_fileter.txt", 'w')

rf = open('C:\Temp\metra2\elog20191111', 'rt')
wf = open("C:\Temp\metra2\elog20191111_filter.txt", 'w')

# dictionary 변수 (Key:Value)
# dic_ex = {"철수": 90, "민수": 85, "영희": 80}
# dic_ex["민수"] = 88   # 수정
# dic_ex["길동"] = 95   # 추가
# del dic_ex["영희"]
# dic_logs = {}

# for line in rf:
while True:
    line = rf.readline()
    if not line: break

    if "CSMl_get_object_attributes" in line :
        pre_line_split=pre_line.split()
        # 년월일 시간
        log_date = pre_line_split[0] + " " + pre_line_split[1]
        # FileNet Process Name
        fn_method = pre_line_split[4]

        line_split = line.split()
        # FileNet 프로세스 PID
        inter_pid = line_split[0]
        # 호출 메소드 (CSMl_get_object_attributes...)
        inter_method = line_split[1].replace(":", "")

        line = rf.readline()
        line_split=line.split()
        obj_id = line_split[1].replace(",", "")
        errnm = line_split[3]

        # dic_logs[inter_pid] = inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + obj_id + "," + errnm
        print(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + obj_id + "," + errnm)
        wf.write(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + obj_id + "," + errnm + "\n")

        pre_line = line
        continue

    if "Object attrs:" in line:
        pre_line_split=pre_line.split()
        # 년월일 시간
        log_date = pre_line_split[0] + " " + pre_line_split[1]
        # FileNet Process Name
        fn_method = pre_line_split[4]

        line_split = line.split()
        # FileNet 프로세스 PID
        inter_pid = line_split[0]
        # Object Max length (Object attrs:)
        obj_mxlen = line_split[3].replace(":", "")

        print(inter_pid + "," + log_date + "," + fn_method + "," + obj_mxlen)
        wf.write(inter_pid + "," + log_date + "," + fn_method + "," + obj_mxlen  + "\n")

        pre_line = line
        continue

    if "CSMl_open_csum_object" in line :
        pre_line_split=pre_line.split()
        # 년월일 시간
        log_date = pre_line_split[0] + " " + pre_line_split[1]
        # FileNet Process Name
        fn_method = pre_line_split[4]

        line_split = line.split()
        # FileNet 프로세스 PID
        inter_pid = line_split[0]
        # 호출 메소드 (CSMl_open_csum_object...)
        inter_method = line_split[1].replace(":", "")

        line = rf.readline()
        line_split=line.split()
        # 조회 DOC ID
        obj_id = line_split[1].replace(",", "")
        obj_page = line_split[2].replace(",", "")
        csum_exists = line_split[4].replace(",", "")

        line = rf.readline()
        line_split=line.split()
        errnm = line_split[0].replace(",", "")
        oh_pp = line_split[1].replace(",", "")

        print(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + obj_id + "," + errnm + "," + obj_page + "," + csum_exists + "," + errnm +  "," + oh_pp)
        wf.write(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + obj_id + "," + errnm + "," + obj_page + "," + csum_exists + "," + errnm+  "," + oh_pp  + "\n")

        pre_line = line
        continue

    if "CSMl_read_object" in line:
        pre_line_split=pre_line.split()
        # 년월일 시간
        log_date = pre_line_split[0] + " " + pre_line_split[1]
        # FileNet Process Name
        fn_method = pre_line_split[4]

        line_split = line.split()
        # FileNet 프로세스 PID
        inter_pid = line_split[0]
        # 호출 메소드 (CSMl_read_object...)
        inter_method = line_split[1].replace(":", "")
        oh_p = line_split[3].replace(",", "")

        line = rf.readline()
        line = rf.readline()
        line_split=line.split()
        # 조회 DOC ID
        bytes_read = line_split[0].replace(",", "")
        errnm = line_split[2].replace(",", "")

        print(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + oh_p + "," + bytes_read + "," + errnm)
        wf.write(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + oh_p + "," + bytes_read + "," + errnm  + "\n")

        pre_line = line
        continue

    if "CSMl_close_csum_object" in line:
        pre_line_split=pre_line.split()
        # 년월일 시간
        log_date = pre_line_split[0] + " " + pre_line_split[1]
        # FileNet Process Name
        fn_method = pre_line_split[4]

        line_split = line.split()
        # FileNet 프로세스 PID
        inter_pid = line_split[0]
        # 호출 메소드 (CSMl_close_csum_object...)
        inter_method = line_split[1].replace(":", "")

        line = rf.readline()
        line_split=line.split()
        csum_exists = line_split[1].replace(",", "")
        errnm = line_split[3].replace(",", "")

        print(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + csum_exists + "," + errnm)
        wf.write(inter_pid + "," + log_date + "," + fn_method + "," + inter_method + "," + csum_exists + "," + errnm  + "\n")

        pre_line = line
        continue

    pre_line = line

rf.close()
wf.close()

