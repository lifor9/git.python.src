# # coding=utf-8
# JSON 문자열을 Python 타입 (Dictionary, List, Tuple 등) 으로 변경하는 것을 JSON Decoding 이라 부른다.
# JSON 디코딩은 json.loads() 메서드를 사용하여 문자열을 Python 타입으로 변경하게 된다.
# JSON 문자열을 Python Dictionary로 변경한 예

# JSON 과 Python 타입 비교
# =========================
# JSON        |     Python
# =========================
# object      |     dict
# array       |     list
# string      |     str
# number(int) |     int
# number(real)|    float
# true        |     True
# false       |     False
# null        |     None
import json

# 테스트용 JSON 문자열
jsonString = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'

# JSON 디코딩
dict = json.loads(jsonString)

# Dictionary 데이타 체크
print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])