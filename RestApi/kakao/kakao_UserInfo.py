import urllib2

API_HOST = 'https://kapi.kakao.com'
APP_KEY = 'Bearer  [YOUR_ACCESS_TOKEN]'
data = {}

def req(path, query, method, data={}):
    url = API_HOST + path
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('QueryString: %s' % query)
    if 'GET' == method:
        req = urllib2.Request(API_HOST + path)
    elif 'POST' == method:
        req = urllib2.Request(API_HOST + path, data)
    req.add_header('Authorization', APP_KEY)
    return urllib2.urlopen(req)

res = req('/v1/user/me', '', 'POST')

print("response status:\n%d" % res.getcode())
print("response info:\n%s" % res.info())
print("response body:\n%s" % res.read())