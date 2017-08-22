'''import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')'''
import bs4

with open('htmlparser.html') as file:
	soup = bs4.BeautifulSoup(file, 'lxml')

event_time = []
event_title = []
event_location = []

for time in soup.select('time'):
		event_time.append(next(time.strings))

for title in soup.select('h3.event-title'):
	event_title.append(title.string)

for location in soup.select('span.event-location'):
	event_location.append(location.string)

for i in range(len(event_time)):
	print('会议时间：%-20s,会议地点：%-70s,会议名称：%s' % (event_time[i], event_location[i], event_title[i]))
