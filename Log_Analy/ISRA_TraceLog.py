# coding=utf-8
import sys


# rf = open('C:\Temp\ISRA_1_0.log', 'rt')
# wf = open("C:\Temp\ISRA_1_0.log_fileter.txt", 'w')

rf = open('C:\Temp\metra2\ISRA_1_0.log', 'rt')
wf = open("C:\Temp\metra2\ISRA_1_0_filter.txt", 'w')

# for line in rf:
while True:
    line = rf.readline()
    if not line: break

    # if "FN_IS_CciConnectionFactory: getConnection(ConnectionSpec): ENTRY" in line :
    #     print(line)
    #     wf.write(line)
    # if "matchManagedConnections" in line :
    #     print(line)
    #     wf.write(line)
    # if "credentials from MC " in line :
    #     print(line)
    #     wf.write(line)
    # if "FN_IS_CciConnectionFactory: getConnection(ConnectionSpec): EXIT" in line :
    #     print(line)
    #     wf.write(line)


    if "GetDocProperties :Start Time" in line :
        print(line)
        wf.write(line)
    if "GetDocProperties :End Time" in line :
        print(line)
        wf.write(line)


    if "GetDocumentContent :Start Time" in line :
        print(line)
        wf.write(line)
    if "FN_IS_CciInteraction : getDocContent(): ENTRY" in line :
        print(line)
        wf.write(line)
    if "FN_IS_CciInteraction : getDocContent(): ENTRY" in line :
        print(line)
        wf.write(line)
    if "FN_IS_ISInterfaceImpl : getDocumentPageArray(): ENTRY" in line :
        print(line)
        wf.write(line)
    if "FN_IS_ISInterfaceImpl : getDocumentPageArray(): EXIT" in line :
        print(line)
        wf.write(line)
    if "FN_IS_CciInteraction : getDocContent(): EXIT" in line :
        print(line)
        wf.write(line)
    if "GetDocumentContent :End Time" in line :
        print(line)
        wf.write(line)


    if "FN_IS_TransportInputStream: read(byte[] b,int offSet,int len): ENTRY" in line :
        print(line)
        wf.write(line)
    if "FN_IS_ISInterfaceImpl : getDocumentNextChunk(): ENTRY" in line :
        print(line)
        wf.write(line)
    if "FN_IS_ISInterfaceImpl : getDocumentNextChunk(): EXIT" in line :
        print(line)
        wf.write(line)
    if "FN_IS_TransportInputStream: read(byte[] b,int offSet,int len): EXIT" in line :
        print(line)
        wf.write(line)

    #
    # if "FN_IS_TransportInputStream: close: ENTRY" in line :
    #     print(line)
    #     wf.write(line)
    # if "FN_IS_CciInteraction : terminateStream(): ENTRY" in line :
    #     print(line)
    #     wf.write(line)
    # if "FN_IS_CciInteraction : terminateStream(): EXIT" in line :
    #     print(line)
    #     wf.write(line)
    # if "FN_IS_TransportInputStream: close: EXIT" in line :
    #     print(line)
    #     wf.write(line)


    if "Cache Handle" in line :
        print(line)
        wf.write(line)
    if "Object Handle" in line :
        print(line)
        wf.write(line)
    if "Bytes To Read" in line :
        print(line)
        wf.write(line)
    if "Doc ID" in line :
        print(line)
        wf.write(line)






rf.close()
wf.close()

