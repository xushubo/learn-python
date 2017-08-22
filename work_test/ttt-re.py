import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import re
import json

def parse(text):
	pattern = re.compile(r'ADDITIONALINFO=.*?\d+.*?:(.*?);', re.S)
	items = re.findall(pattern, text)
	for item in items:
		yield item

def write_to_file(content):
	with open('result11.txt', 'a', encoding='utf-8') as f:
		f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main():
	with open('ttt.txt') as f:
		text = f.read()
	parse_text = parse(text)
	for item in parse_text:
		write_to_file(item)

if __name__ == '__main__':
	main()