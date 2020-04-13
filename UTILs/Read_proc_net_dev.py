# # coding=utf-8
# python을 이용 /proc/net/dev 출력을 key:value 쌍으로 파싱하기

# ==============================================
lines = open("/proc/net/dev", "r").readlines()

columnLine = lines[1]
_, receiveCols , transmitCols = columnLine.split("|")
receiveCols = map(lambda a:"recv_"+a, receiveCols.split())
transmitCols = map(lambda a:"trans_"+a, transmitCols.split())

cols = receiveCols+transmitCols

faces = {}
for line in lines[2:]:
    if line.find(":") < 0: continue
    face, data = line.split(":")
    faceData = dict(zip(cols, data.split()))
    faces[face] = faceData

import pprint
pprint.pprint(faces)

# ==============================================
from __future__ import with_statement
import re
import pprint

ifaces = {}

with open('/proc/net/dev') as fd:
    lines = map(lambda x: x.strip(), fd.readlines())

lines = lines[1:]

lines[0] = lines[0].replace('|', ':', 1)
lines[0] = lines[0].replace('|', ' ', 1)
lines[0] = lines[0].split(':')[1]

keys = re.split('\s+', lines[0])
keys = map(lambda x: 'rx' + x[1] if x[0] < 8 else 'tx' + x[1], enumerate(keys))

for line in lines[1:]:
    interface, values = line.split(':')
    values = re.split('\s+', values)

    if values[0] == '':
        values = values[1:]

    values = map(int, values)

    ifaces[interface] = dict(zip(keys, values))

pprint.pprint(ifaces)

# ==============================================
dev = open("/proc/net/dev", "r").readlines()
header_line = dev[1]
header_names = header_line[header_line.index("|")+1:].replace("|", " ").split()

values={}
for line in dev[2:]:
    intf = line[:line.index(":")].strip()
    values[intf] = [int(value) for value in line[line.index(":")+1:].split()]

    print intf,values[intf]
