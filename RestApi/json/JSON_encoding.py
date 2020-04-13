# coding=utf-8
# Python Object (Dictionary, List, Tuple 등) 를 JSON 문자열로 변경하는 것을 JSON Encoding 이라 부른다.
# JSON 인코딩을 위해서는 우선 json 라이브러리를 import 한 후,
# json.dumps() 메서드를 써서 Python Object를 문자열로 변환하면 된다.

# customer 라는 Python Dictionary 객체를 JSON 문자열로 인코딩하는 예
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

# 테스트용 Python Dictionary
customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

# JSON 인코딩
jsonString = json.dumps(customer)

# 문자열 출력
print(jsonString)
print(type(jsonString))  # class str