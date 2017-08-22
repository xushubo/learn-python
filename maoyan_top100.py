import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
import re
import json

def get_one_page(url):
	try:
		response = requests.get(url)
		if response.status_code == 200:
			return response.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?'
		                +r'>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">'
		                +r'(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield {
			'index': item[0],
			'image': item[1],
			'title': item[2],
			'actor': item[3].strip()[3:],
			'time': item[4][5:],
			'score': item[5]+item[6]
		}

def write_to_file(content):
	with open('result.txt', 'a', encoding='utf-8') as f:
		f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
	url = 'http://maoyan.com/board/4?offset=' + str(offset)
	html = get_one_page(url)
	for item in parse_one_page(html):
		print(item)
		write_to_file(item)

if __name__ == '__main__':
	pool = Pool()
	pool.map(main, [i*10 for i in range(10)])