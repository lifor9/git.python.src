#!/app/python/bin/python
from urllib.request import urlopen
from urllib.parse import urlencode,unquote,quote_plus
import urllib

url = 'http://apis.data.go.kr/B552061/jaywalking/getRestJaywalking'

queryParams = '?' + urlencode({ quote_plus('servicekey') : 'YourServiceKey',
    quote_plus('LAYERS') : 'frejaywalking',
    quote_plus('FORMAT') : 'image/png',
    quote_plus('TRANSPARENT') : 'true',
    quote_plus('SERVICE') : 'WMS',
    quote_plus('VERSION') : '1.1.1',
    quote_plus('REQUEST') : 'GetMap',
    quote_plus('SRS') : 'EPSG:900913',
    quote_plus('BBOX') : '14142684.718103,4505504.1936344,14147576.687913,4510396.1634438',
    quote_plus('width') : '2024',
    quote_plus('height') : '1838',
    quote_plus('srs') : 'EPSG:900913',
    quote_plus('searchYearCd') : '2015052',
    quote_plus('siDo') : '11',
    quote_plus('guGun') : '320' })

request = urllib.request.Request(url+unquote(queryParams))
print ('Your Request:\n'+url+queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print ("\nResult:")
print (response_body)
print ("\nDataType of Result Data:")
print (type(response_body))