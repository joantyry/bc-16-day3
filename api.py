from urllib2 import Request, urlopen, URLError

'''
This is an API that requests information from the google page and displays it from index [1]
to index [500]
'''

request = Request('http://google.com/')

try:
	response = urlopen(request)
	google = response.read()
	print google [1: 500]
except URLError, e:
    print 'No google page found:', e


