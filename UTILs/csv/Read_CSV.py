import csv

# WITH 문 이용
with open('some.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

# WITH 문을 사용하지 않는 경우
f = open('some.csv', 'rb')
reader = csv.reader(f)
for row in reader:
    print row
f.close()

