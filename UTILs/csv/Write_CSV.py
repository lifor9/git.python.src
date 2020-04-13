# coding=utf-8
import csv

# with open(newfilePath, "w") as f:
#     writer = csv.writer(f)
#     for row in rows:
#         writer.writerow(row)

dic = {firstcol,secondcol} #dictionary
csv = open('result.csv', "w")
for key in dic.keys():
    row ="\n"+ str(key) + "," + str(dic[key])
    csv.write(row)

from itertools import zip_longest
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['f', 'g', 'i', 'j']
d = [list1, list2]
export_data = zip_longest(*d, fillvalue = '')
with open('numbers.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("List1", "List2"))
      wr.writerows(export_data)
myfile.close()