import string

fname = raw_input('Enter file :')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened : ', fname
    exit()

counts = dict()

for line in fhand :
    # string.translate(s, table[, deletechars])
    # (만약존재한다면) deletechars에있는모든문자를삭제한다.그리고 나서 순서
    # 수(ordinal)로 색인된 각 문자를 번역하는 256-문자열테이블(table)을사용해서
    # 문자를 번역한다.만약 테이블이 None이면,문자 삭제 단계만 수행된다.
    # string.punctuation -->  '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else :
            counts[word] += 1

print counts


fhand = open('mbox-short.txt')
for line in fhand:
    # 문자열 오른쪽 끝에서 부터 공백을 벗겨내는 rstrip 메쏘드
    line = line.rstrip()
    # From: 으로 시작여부 확인
    # startswith 메쏘드는 참, 거짓 같은 불 값(boolean value)을 반환
    if line.startswith('From:') :
        print line