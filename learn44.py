class Chain(object):
	def __init__(self, path=''):
		self.path = path

	def users(self, user):
		return Chain('/users/%s' % (user))

	def __getattr__(self, path):
			return Chain('%s/%s' % (self.path, path))

	def __str__(self):
		return self.path
	__repr__ = __str__


print(Chain().users('Michael').repos)
print(Chain().status.usegf.dder)

class Chain1(object):
	def __init__(self, path='GET '):
		self.path = path

	def __getattr__(self, path): # 使用实例不存在的属性时，会尝试用该函数解释
		return Chain1('%s/%s' % (self.path, path))

	def __call__(self, path):
		return Chain1('%s/%s' % (self.path, path))

	def __str__(self):
		return self.path

	__repr__ = __str__


print(Chain1().users('Michael').repos)
print(Chain1().users('Michael').age('2015-1-4').repos)