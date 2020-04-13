# coding=utf-8
import sys


# rf = open('C:\Temp\ISRA_1_0_RPC.log', 'rt')
# wf = open("C:\Temp\ISRA_1_0_RPC_fileter.txt", 'w')

rf = open('C:\Temp\metra2\ISRA_1_0_RPC.log', 'rt')
wf = open("C:\Temp\metra2\ISRA_1_0_RPC_filter.txt", 'w')


# for line in rf:
while True:
    line = rf.readline()
    if not line: break

    if "Creating socket connection" in line :
        print(line)
        wf.write(line)
    if "Opened socket connection from port" in line :
        print(line)
        wf.write(line)
    if "Closing socket connection from port" in line :
        print(line)
        wf.write(line)
    if "Terminal name" in line :
        print(line)
        wf.write(line)
    if "Document Id" in line :
        print(line)
        wf.write(line)
    if "Deserialized Object" in line :
        print(line)
        wf.write(line)
    if "CSM Session Handle" in line :
        print(line)
        wf.write(line)
    if "FN_IS_RPC_ServiceConnectionManager getCSM(): ENTRY" in line :
        print(line)
        wf.write(line)
    if "FN_IS_RPC_ServiceConnectionManager getCSM(): EXIT" in line :
        print(line)
        wf.write(line)

rf.close()
wf.close()

