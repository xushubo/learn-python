def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return
		print('[COMSUMER]consuming %s...' % n)
		r = '200 OK'


def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n += 1
		print('[PRODUCE] producing %s...' % n)
		r = c.send(n)
		print('[PRODUCE] consumer return:%s' % r)
	c.close()

c = consumer()
produce(c)