def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'  #启动Python解释器时可以用-O参数来关闭assert,关闭后，你可以把所有的assert语句当成pass来看。
	return 10 / n

def main():
#	foo('0')
	foo('1')
main()



import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)