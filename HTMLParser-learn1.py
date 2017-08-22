import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.event_time = []
		self.event_title = []
		self.event_location = []
		self.in_time = False
		self.in_title = False
		self.in_location = False

	def handle_starttag(self, tag, attrs):
		def _attr(attrlist, attrname):
			for i in attrlist:
				if attrname == i[0]:
					return i[1]
			return None
		if tag == 'h3' and _attr(attrs, 'class') == 'event-title':
			self.in_title = True
		if tag == 'time':
			self.in_time = True
		if tag == 'span' and _attr(attrs, 'class') == 'event-location':
			self.in_location = True

	def handle_data(self, data):
		if self.in_time:
			self.event_time.append(data)
			self.in_time = False
		if self.in_title:
			self.event_title.append(data)
			self.in_title = False
		if self.in_location:
			self.event_location.append(data)
			self.in_location = False


if __name__ == '__main__':
	parser = MyHTMLParser()
	with open('htmlparser.html') as f:
		htmltext = f.read()
		parser.feed(htmltext)
	for i in range(len(parser.event_time)):
		print(parser.event_time[i], parser.event_title[i], parser.event_location[i])
