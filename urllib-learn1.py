import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from urllib import request
import re

def fetch_xml(url):
	with request.urlopen(url) as f:
		print('Status:', f.status, f.reason)
		for k, v in f.getheaders():
			print('%s: %s' % (k, v))
		html = f.read().decode('utf-8')
	pattern_one = re.compile(r'<yweather:location.*?city="(.*?)".*?country="(.*?)".*?region="(.*?)".*?/>', re.S)
	pattern_two = re.compile(r'<yweather:forecast.*?date="(.*?)".*?day="(.*?)".*?high="(.*?)".*?low="(.*?)".*?text="(.*?)".*?/>', re.S)
	location_info = re.findall(pattern_one, html)
	items = re.findall(pattern_two, html)
	weather = {}
	weather['city'] = location_info[0][0]
	weather['country'] = location_info[0][1]
	weather['region'] = location_info[0][2]
	for item in items:
		weather[item[1]] = {}
		weather[item[1]]['data'] = item[0]
		weather[item[1]]['high'] = item[2]
		weather[item[1]]['low'] = item[3]
		weather[item[1]]['text'] = item[4]
	return weather

if __name__ == '__main__':
	weather_result = fetch_xml('https://query.yahooapis.com/v1/public/yql?'
		+'q=select%20*%20from%20weather.forecast%20where%20'
		+'woeid%20in%20(select%20woeid%20from%20geo.places(1)'
		+'%20where%20text%3D%22hangzhou%2C%20china%22)&format'
		+'=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
	print(weather_result)