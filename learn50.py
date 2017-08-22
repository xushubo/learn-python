import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar(0)
	except Exception as e:
		print('Error:', e)
	finally:
		print('finally...')

main()

def foo1(s):
	return 10 / int(s)

def bar1(s):
	return foo1(s) * 2

def main1():
	try:
		bar1('0')
	except Exception as e:
		logging.exception(e)

main1()
print('end')