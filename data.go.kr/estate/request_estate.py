# Python 샘플 코드 #
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'lSFopbktF%2BpsrgqDAWpyBLVJZHRAQ6VwewHd3%2FZm%2ByJIlGCRr1hQi%2F9WUXa%2B4xeYtMnS1sasO%2FM7EYFo9d4qhQ%3D%3D', quote_plus('LAWD_CD') : '11110', quote_plus('DEAL_YMD') : '201512', quote_plus('serviceKey') : 'lSFopbktF%2BpsrgqDAWpyBLVJZHRAQ6VwewHd3%2FZm%2ByJIlGCRr1hQi%2F9WUXa%2B4xeYtMnS1sasO%2FM7EYFo9d4qhQ%3D%3D' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body