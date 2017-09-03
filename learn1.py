print('I\'m ok!')
print('I\'m learing\nPython')
print('\\\n\\')#转义符：\
print('\\\t\\')
print('''line1
line2
line3''')#用'''...'''的格式表示多行内容
print(r'\\\\n\\')#用r''表示''内部的字符串默认不转义
print(r'''line1\t\\\\
line2\\\n\\
	line3''')
def gen():
	yield from subgen()
def subgen():
	while True:
		x = yield
		yield x + 1
def main():
	g = gen()
	next(g)                # 驱动生成器g开始执行到第一个 yield
	retval = g.send(1)     # 看似向生成器 gen() 发送数据
	print(retval)          # 返回2
	g.throw(StopIteration) # 看似向gen()抛入异常


dic = {'id': 123, 'name': 'Michile'}
t = dic.get('id')

print(t)
