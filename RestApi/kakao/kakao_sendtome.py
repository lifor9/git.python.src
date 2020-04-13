import requests

API_HOST = 'https://kapi.kakao.com'
headers = {'Authorization': 'Bearer [YOUR_ACCESS_TOKEN]'}
data = {}

def req(path, query, method, data={}):
    url = API_HOST + path

    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    if method == 'GET':
        return requests.get(url, headers=headers)
    else:
        return requests.post(url, headers=headers, data=data)

template_id = 0 # 메시지 템플릿 v2의 아이디
params = {"template_id": {template_id}, "templates_args":{"name":"홍길동"}}
resp = req('/v2/api/talk/memo/send', '', 'POST', params)
print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
print("response body:\n%s" % resp.text)