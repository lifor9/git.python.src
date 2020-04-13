#  coding=utf-8
import requests

API_HOST = 'https://kapi.kakao.com'
# headers = {'Authorization': 'Bearer [YOUR_ACCESS_TOKEN]'}

# def req(path, query, method, data={}):
#     url = API_HOST + path
#     print('HTTP Method: %s' % method)
#     print('Request URL: %s' % url)
#     print('Headers: %s' % headers)
#     print('QueryString: %s' % query)
#
#     if method == 'GET':
#         return requests.get(url, headers=headers)
#     else:
#         return requests.post(url, headers=headers, data=data)

# resp = req('/v1/user/me', '', 'GET')

RestApikey = 'f2a21e3ae2dca9c4c06d80170cd5f01c'
# path = '/oauth/token'
path = '/oauth/authorize'
# payload = 'grant_type=authorization_code&client_id=' + RestApikey + '&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Foauth&code=' + str(code)

'/oauth/authorize?client_id=' + RestApikey + '&redirect_uri=http://localhost:5000&response_type=code'
payload = 'grant_type=authorization_code&client_id=' + RestApikey + '&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Foauth&code=' + str(code)
headers = {
    'Content-Type' : "application/x-www-form-urlencoded",
    'Cache-Control' : "no-cache"
}

response = requests.request("POST", API_HOST+path, data=payload, headers=headers)
# resp = req(, '', 'GET')
print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
print("response body:\n%s" % resp.text)