class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n==0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

try:
	foo('0')
except FooError as e:
	print('FooError:', e)



def fod(s):
	n = int(s)
	if n==0:
		raise ValueError('invalid value: %s' % s)
	return 10 / n

def bar():
	try:
		fod('0')
	except ValueError as e:
		print('ValueError!')
		raise   #raise语句如果不带参数，就会把当前错误原样抛出


try:
	bar()
except ValueError as e:
	print('one more time!!!!')

try:
	try:
		10 / 0
	except ZeroDivisionError as e:
		raise ValueError('input error') #在except中raise一个Error，还可以把一种类型的错误转化成另一种类型
except ValueError as e:
	print('ValueError!!!')