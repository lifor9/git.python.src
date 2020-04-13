import requests
import json

API_HOST = "https://tms.dev-redcap.co.kr/tms-web/smsReq"
headers = {"Content-Type":"application/json","charset":"UTF-8"}
data = {
    "smsReqList":[
        {
            "serialNumber": "111",
            "mtType" : "SM",
            "phoneNumber": "01088862022",
            "senderId": "tms",
            "messageGroupKey": "Immediately_sending",
            "callback": "0220014500",
            "message": "SMS 문자메시지 입니다."
        }
    ]
}

response = requests.post(API_HOST, data=data, headers=headers)

print("response status:\n%d" % response.status_code)
print("response headers:\n%s" % response.headers)
print("response body:\n%s" % response.text)