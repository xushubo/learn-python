try:
	print('try...')
	r = 10/0
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')

tab_input = input('请输入除数：')
try:
	print('try...')
	r = 10 / int(tab_input)
	print('result:', r)
except ValueError as e:
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:', e)
else:    #可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
	print('no error!')
finally:
	print('finally...')
print('END')